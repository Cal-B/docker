# Installation 
Running any automatic build options actually borks this install, you have to build everything manually.

To add new Openaddress data, you'll need to [download an OA archive](https://batch.openaddresses.io/data) and parse the individual city .csvs at the top of the archive with `ls us/nc/ | grep .csv | awk 'NF { print "\"us/nc/"$0"\","}'` and replace the current address data in `pelias.json`.

To add a new WhosOnFirst region, use [Spelunker](https://spelunker.whosonfirst.org/) and search for your state, and filter by region. You can put the resulting code into the `importPlace` array inside `pelias.json`.

To change the Tiger statecode, refer to [this page](https://github.com/pelias/interpolation).

Getting `Creating extract at /data/placeholder/wof.extract
/code/pelias/placeholder/node_modules/pelias-blacklist-stream/parser.js:11
    throw new Error( 'file not found' );` ?
Create a `synonyms` and `blacklist` folder in the project folder, and place a blank `osm.txt` inside the blacklist folder 

Sometimes pelias will create a `custom_street.txt` and `custom_name.txt` directory inside `synonyms`, delete these and make text files in their place 

```bash
pelias compose pull
pelias elastic start
pelias elastic wait
pelias elastic create
pelias download all
pelias prepare polylines
pelias prepare interpolation
pelias prepare placeholder
pelias import wof
pelias import oa
pelias import osm
pelias import polylines
pelias compose up
```