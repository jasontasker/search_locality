# Search Locality Problem

## Details

As a staff researcher, you must repeatedly search through a set of plain text documents in order to do your work.

A common need is to find documents where two different topics or search terms are discussed in the same context, for example: oncology and morbidity, or virtualization and agility.

"Context" within a document can be ambiguous or ill-defined, but in this case, "context" is defined as the two search terms occurring within N words of each other irrespective of sentence, paragraph or page boundaries.

Using a programming language of your choice, develop a piece of software that can iterate over all the plain text documents in a directory and return the set of documents where two search terms occur within N words of each other.

### Extra credit:
In addition to allowing two search terms, allow the user to specify phrases instead of terms, e.g. "Dr. Fowler" and "Continuous Delivery"



## Requirements
- Python >= 2.7 re, os, glob, and argparse modules


## Default Settings
- Min: "0" - Minimum words between contexts needed
- Max: "10" - Maximum words between contexts needed
- Context1: "context1" - *Required* Define first context to search for
- Context2: "context2" - *Required* Define second context to search for
- Directory: "." - Define directory to search for files
- Extension: "txt" - Define file extension to search for

## Installation
Download the project:
```sh
git clone https://github.com/jasontasker/search_locality.git
```

## Execution
##### Install 
```sh
cd search_locality
python search.py --context1 "vim tutor" --context2 "follow the instructions" --directory /usr/share/vim --min 0 --max 5 --extension txt
```


## Usage
```text
usage: search.py [-h] [--min MIN_WORDS] [--max MAX_WORDS] --context1 CONTEXT1
                 --context2 CONTEXT2 [--directory DIRECTORY]
                 [--extension EXTENSION]
```

## Sample Output
```text
This file matches the 2 contexts:
/usr/share/vim/vim73/tutor/README.txt
```

