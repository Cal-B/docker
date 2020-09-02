# Installation 
Running any automatic build options actually borks this install, you have to build everything manually.

To add new Openaddress data, you'll need to [download an OA archive](https://batch.openaddresses.io/data) and parse the individual city .csvs at the top of the archive with `ls us/nc/ | grep .csv | awk 'NF { print "\"us/nc/"$0"\","}'` and replace the current address data in `pelias.json`.

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