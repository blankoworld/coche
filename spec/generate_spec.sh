#!/usr/bin/env bash

import_ext=".md"
export_ext=".html"
header="header.tmpl"
footer="footer.tmpl"

for file in *.md
do
  name=`basename $file $import_ext`
  output="${name}${export_ext}"
  cat $header > $output
  python3 -m markdown $file >> $output
  cat $footer >> $output
done
