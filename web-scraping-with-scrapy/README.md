## [On-line tutorial](https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/)
Based on this on-line tutorial, I played with scrapy within a docker images

### Usage
#### Run container
```
sudo docker run --rm -it -v "$(pwd):/notebooks" itamtao/scrapy /bin/zsh
```

#### Run scrapy
* Simple version

```
scrapy crawl stack
# You can render the output to a JSON file with this little command:
crapy crawl stack -o items.json -t json
```

* It crawls through the pagination links at the bottom of each page and scrapes the questions (question title and URL) from each page.

```
scrapy crawl stack_crawler
```
