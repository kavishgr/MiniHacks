package main

import(
	"fmt"
	"net/url"
	"net/http"
	"strings"
	"github.com/anaskhan96/soup"
	"path/filepath"
	"sync"
	"github.com/schollz/progressbar"
	"os"
	"io"
	"log"
)

func extractdomain(domain string) string{
	// url.Parse will return a URL struct, for which you can extract info such host, port, scheme, etc
	result, _ := url.Parse(domain)
	// get the hostname: www.artsy.net, and trim "www." -> artsy.net 
	extractdomain := strings.TrimPrefix(result.Hostname(), "www.")
	// return "artsy.net"
	return extractdomain
}

// parse the domain extracted above, and cliurl 
func getArtworksUrlsPlusTitle(domain, cliurl string) ([]string, string){
	// the slice/list below will store the artworks url found in cliurl, which will contain duplicates
	// an artwork looks like this: /artwork/tod-papageorge-malibu-1975-3
	var dupeArtworksUrls []string
	// http GET request cliurl
	resp, _ := soup.Get(cliurl)
	// parse it in HTMLParse to get HTML objects
	doc := soup.HTMLParse(resp)
	// find all <a> tags or hyperlinks
	links := doc.FindAll("a")
	for _, link := range links {
		// for each <a> tag find the href
		artwork := link.Attrs()["href"]
		// if href contains the keywork "artwork"
		if strings.Contains(artwork, "artwork"){
			// append https:// and domain name to look like this:
			// https://www.artsy.net/artwork/tod-papageorge-malibu-1975-3
			artwork = fmt.Sprintf("https://%s%s", domain, artwork)
			// append it in the list(there will be duplicates)
			dupeArtworksUrls = append(dupeArtworksUrls, artwork)
		}	
	}

	//remove duplicates and save the unique urls in artworkUrls[]
	allKeys := make(map[string]bool)
    artworksUrls := []string{}
    for _, item := range dupeArtworksUrls {
        if _, value := allKeys[item]; !value {
            allKeys[item] = true
            artworksUrls = append(artworksUrls, item)
        }
    }

    // get webpage title to create a directory with it later
    var webtitles []string
    webpagetitles := doc.FindAll("title")
    for _, webpagetitle := range webpagetitles{
    	webtitles = append(webtitles, webpagetitle.Text())
    }

    // return list of artworks and webpage title
	return artworksUrls, webtitles[0]
}

// parse the list of artworks found above
func getArtworksJpegs(artworks []string) map[string]string{
	// map to store image name and image url
	// example: tod-papageorge-malibu-1975-3:https://dfsd66868.cloud/normalized.jpg
	artworkMap := make(map[string]string)
	// for each artwork https://www.artsy.net/artwork/tod-papageorge-malibu-1975-3: 
	for _, artwork := range artworks{
		// parse the URL
		artworknametemp, _ := url.Parse(artwork)
		// extract the last path. example: tod-papageorge-malibu-1975-3
		// save it in the variable artworkname
		artworkname := filepath.Base(fmt.Sprintf("%s", artworknametemp))
		// http GET artwork url https://www.artsy.net/artwork/tod-papageorge-malibu-1975-3
		resp, _ := soup.Get(artwork)
		// Parse the HTML
		doc := soup.HTMLParse(resp)
		// find all <link> tags
		artworkLinkTags := doc.FindAll("link")
		// for each <link> tag
		// <link> tag looks like this(all the below comments in one line):
		// <link data-rh="" rel="preload" as="image" 
		// href="https://d7hftxdivxxvm.cloudfront.net?resize_to=fit
		// &amp;width=800&amp;height=533&amp;quality=80
		// &amp;src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Futz-gGmqT9GpcnmUe4lmNA%2Fnormalized.jpg" imagesrcset="https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&amp;width=800&amp;height=533&amp;quality=80&amp;src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Futz-gGmqT9GpcnmUe4lmNA%2Fnormalized.jpg 1x, https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&amp;width=1600&amp;height=1066&amp;quality=50&amp;src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Futz-gGmqT9GpcnmUe4lmNA%2Fnormalized.jpg 2x" data-reactroot=""/>
		for _, linktag := range artworkLinkTags {
			// find the href
			eachArtworkJpeg := linktag.Attrs()["href"]
			// if href url ends with jpg
			if strings.HasSuffix(eachArtworkJpeg, "jpg"){
				// parse it in url.Parse to get a URL object
				parseJpeg, _ := url.Parse(eachArtworkJpeg)
				// pcall the Query method or function to extract specific parts from the URL
				extractSrcFromHref := parseJpeg.Query()
				// extract the src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Futz-gGmqT9GpcnmUe4lmNA%2Fnormalized.jpg
				// it will decoded by default
				// to look like this: 
				// https://d32dm0rphc51dk.cloudfront.net/utz-gGmqT9GpcnmUe4lmNA/normalized.jpg
				// save it in the map like so: 
				// tod-papageorge-malibu-1975-3:https://d32dm0rphc51dk.cloudfront.net/utz-gGmqT9GpcnmUe4lmNA/normalized.jpg
				artworkMap[artworkname] = extractSrcFromHref.Get("src")
			}
		}	
	}
	// return the map
	return artworkMap

}

func main(){
	// cliurl := "https://www.artsy.net/show/crane-kalman-brighton-slim-aarons-summer"
	cliurl := os.Args[1]
	// extract the domain: artsy.net
	domain := extractdomain(cliurl)
	// get all artworks url and web page title
	artworks, title := getArtworksUrlsPlusTitle(domain, cliurl)

	fmt.Println(title)

	// parse artwork urls, get jpeg url, and artwork name
	artworksJpegs := getArtworksJpegs(artworks)
	
	// spawn number of goroutines/workers based on number of artworks
	workers := len(artworksJpegs)

	// add goroutines/workers in queue
	var wg sync.WaitGroup
	wg.Add(workers)

	// create artwork directory named as the webpage title
	err := os.Mkdir(title, 0750)
	if err != nil && !os.IsExist(err){
		log.Fatal(err)
	}

	// change into the directory
	if err = os.Chdir(title); err != nil {
		log.Fatal(err)
	}

	// loop over the map 
	// download all jpgs concurrently
	for imgname, url := range artworksJpegs{
		// for each url, spawn a worker
		go func(imgname, url string){
			// http GET the url
			req, _ := http.NewRequest("GET", url, nil)
			resp, _ := http.DefaultClient.Do(req)
			defer resp.Body.Close()
			// create the file in which the image will be downloaded
			// artworkname.jpg
			imgplusjpg := fmt.Sprintf("%s.jpg", imgname)
			fimg, _ := os.OpenFile(imgplusjpg, os.O_CREATE|os.O_WRONLY, 0644)
			defer fimg.Close()
			// display a progress bar for each download
			bar := progressbar.DefaultBytes(
				resp.ContentLength,
				fmt.Sprintf("downloading %s", imgplusjpg),
			)
			// write image data to file on disk
			io.Copy(io.MultiWriter(fimg, bar), resp.Body)
			// worker's job is done
			wg.Done()
		}(imgname, url)
	}

	// wait for all workers to finish, then main() can exit
	wg.Wait()


}

