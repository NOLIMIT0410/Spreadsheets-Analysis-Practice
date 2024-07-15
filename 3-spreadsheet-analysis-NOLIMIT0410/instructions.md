# Instructions

A little assignment to practice finding data, munging it, and analyzing it in a spreadsheet program.

The goals of this assignment are to:

- "scrub", "munge", or "clean" a datafile using Python 3
- import the text data file into an Microsoft Excel, Google Sheets, Apple Numbers, or Libre Office spreadsheet
- produce statistical results based on the data using the database-like functions in the spreadsheet program of your choice
- save the spreadsheet as a proper spreadsheet file (e.g. `.xslx`, `.numbers`, `.ods`)

## Part 1: Data selection and retrieval

### Select a data source

First, you will need to select a datafile to work from. For this assignment, please select any reputable data source that is of interest to you. Download the data in a plain text data format, not a spreadsheet-specific file format.

### Where to find data

There are many data sources available via NYU Libraries data portal. Note that you are encouraged to visit [Data Services](http://guides.nyu.edu/datasources) on the 5th Floor of Bobst Library for help finding data. A few recommended to our class by the librarians:

Librarian Vicky Rampin has shared an [excellent set of helpful slides about finding data](https://drive.google.com/file/d/1rt7ZnG70_e-Uwje8lrnoKQlv1rICdUY7/view).

Librarian Andrew Battista has shared specific links to data portals that may be the first step of your journey towards the data of your dreams:

- [Data Sources by Topic](http://guides.nyu.edu/content.php?pid=352851&sid=2886542) (especially NYC data sources)
- NYC Department of City Planning's [Bytes of the Big Apple](http://www.nyc.gov/html/dcp/html/bytes/applbyte.shtml)
- [NYC Open Data](https://nycopendata.socrata.com/) project
- [Inter-University Consortium for Political and Social Research (ICPSR)](http://www.icpsr.umich.edu/icpsrweb/landing.jsp) (in particular, data on crime).
- [International Monetary Fund (IMF) eLibrary Data](https://www.imf.org/external/data.htm)

Other sample data sets that might interest you:

- [MusicBrainz](http://musicbrainz.org/)
- [Baseball statistics](http://www.baseball-reference.com/)
- [Bloomberg Financial Data](http://www.bloomberg.com/markets/stocks/)
- [Bureau of Labor Statistics](http://www.bls.gov/data/)
- [US Census](http://www.census.gov/geo/maps-data/data/gazetteer.html)

#### Additional resources

You might also consider consulting with a [Subject Librarian at the library](http://library.nyu.edu/research/lib_arc.html) if you prefer for additional data sources or data sources in your specific field of study.

### Save the data

Save the original raw data file of your choice into the `data` directory.

### What not to do

Please do NOT use [average surface temperature data from NASA](http://data.giss.nasa.gov/gistemp/#tabledata). You will NOT get credit for a project retrieving data from this or another data set we have discussed as an example.

Also, do not choose a data file already selected by another student in the course. Check the `#data-dibs` Discord channel for claims on any data set. If there are none, then you are welcome to use that data set and claim it as yours in that Discord channel.

## Part 2: Data scrubbing

### Use Python to do something

In almost all cases, you will need to "clean up", "scrub", or "munge" the data before you can use it in a spreadsheet. If you are lucky enough to pick data that are already in usable format, use Python to modify the data in some major and discernible ways such as removing unnecessary columns or adding computed columns.

### Save the modified data

Write a Python program in the file named `munge.py` to read in the data file which you have downloaded or copied from the Internet; and then the Python program should write out a new file that is ready for data analysis, named `clean_data.csv`, into the `data` directory .

### Repeatability

Your program should be written to work consistently and repeatedly with the dataset of your choice regardless of how many lines of data are in the file. In other words, the program should be scalable and not based on idiosyncratic strategies such as, "for the third row do this... for the fourth row do that... " etc.

### Other scrubbing tools

If there are some scrubbing tasks that you simply cannot complete in Python, you are welcome to use a text editor or spreadsheet program to complete the scrubbing. But any such work must be relatively minor and documented thoroughly in the report you will write so that someone else can repeat the process without difficulty.

## Part 2: Data analysis in a spreadsheet

### Import data into a spreadsheet

Import your newly-scrubbed data file into a sheet in the spreadsheet program of your choice, such as Microsoft Excel, Google Sheets, Apple Numbers, or Libre Office. If it doesn't import correctly, keep working on the scrubbing of your data until it does!

### Calculate aggregate statistics

Use formulas to calculate four different aggregate statistics based on your data, such as mean, maximum, minimum, etc of one or more entire columns in the data. Place a clear label for each statistic in a neighboring cell.

### Calculate aggregate statistics with conditions

Use formulas to calculate four different aggregate statistics based on specific criteria you define, such as mean, maximum, minimum, etc of only those rows that match the given criterion or multiple criteria. Place a clear label for each statistic in a neighboring cell so that someone viewing your spreadsheet can easily understand exactly what each statistic represents.

Be sure to use the database-like functions appropriate to your spreadsheet program (e.g. `AVERAGEIF`, `MAXIF`, `MINIF`, `SUMIF`, etc for most spreadsheet programs; Microsoft Excel also has `DAVERAGE`, `DMAX`, `DMIN`, etc ).

### Do some further analysis

Perform further, more complex analysis that shows some interesting insights into your data set by using one or more of the following techniques:

- pivot table
- chart

### Save the spreadsheet

Save the spreadsheet as a proper spreadsheet file (e.g. `.xslx`, `.numbers`, `.ods`) into your `data` directory. So you now have at least 3 files in the `data` directory:

1. the original data file
1. the munged data file
1. the spreadsheet file.

### What to do for very large data files

Check the size of each of your data files. If any of your files is larger than `50MiB`, you should not include it in the files you upload to GitHub. GitHub currently blocks files larger than `100 MiB` - [see their notes on dealing with large files](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

If any of your files is greater than this size, you may upload them to a cloud storage service such as Google Drive or Box and then provide a clearly-labeled link to the files in the report you will write in the `README.md` file (more on that below). In that case, also edit the [.gitignore](./.gitignore) file to exclude the data files from being uploaded to GitHub by adding the following line:

      data/*

This way, when you `push` or "sync" your modified files to GitHub, the data files will not be included.

### Write a report

Write a report which displays the data and the results in the file named [README.md](./README.md).

This report should be well-written and well-formatted using Markdown code - refer to this [guide to using Markdown](https://guides.github.com/features/mastering-markdown/).

The report must include:

Data set details:

- The origin of your data set - what is it and where does it come from. Include a link to the URL of the source.
- What format the original data file was in (CSV, JSON, or other).
- Display some of the raw data from the original data file (the first 20 rows is enough). Use Markdown's ability to display tables - see the examples in the Markdown guide linked above.
- Describe the problems that were present in the data and the scrubbing tasks that were necessary to prepare your data set for import into a spreadsheet - include scrubbing done in Python, a text editor, or any other tool. Be specific with examples of the problems in the original data and the way in which those were solved. Feel free to show small snippets of relevant code - see the examples of code "syntax highlighting" in the Markdown guide linked above.
- Links to your data files (the original raw data, the munged data, and the spreadsheet file including the formulas and charts). These can be links to files in your own repository or links to the files stored in a cloud storage service if your files are too large to be included in your own repository.

Analysis:

- Describe each of the aggregate statistic you have calculated - include a description of each and describe any insights the statistic shows that may not be obvious to someone just viewing the raw data.
- If using a pivot table for analysis, include a Markdown table showing a sample of the results of the pivot table (no more than 20 rows, please), along with a short description of what the results show and any insights they offer.
- If using a chart for visualization, include the chart image in the report, with a short description of what the image shows and any insights it offers. See the Markdown guide linked above for details of showing an image.

## Part 3: Extra credit

You may do one, two, or neither of these extra credit options as you prefer:

### Option 1: Scraping data

There is an extra credit option to use Python to retrieve the data directly from a webpage using [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request). If you do "scrape" data off the web in this way, feel free to use the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) library, or another parser module in python to assist in removing the HTML from the page and parsing the document, if necessary.

### Option 2: Big or complex data

Extra Credit is available for examples which tackle large and/or complex data tables. A large data set, for our purposes, being defined as thousands of rows.

### Requesting extra credit

If you believe you deserve extra credit, include a sub-heading at the bottom of your `README.md` document explaining why you believe you deserve it.

```markdown
...

## Extra-credit

This assignment deserves extra credit because iste numquam eos et repudiandae sint enim. Rerum enim voluptas voluptatem consequuntur. Sed atque deserunt nihil eius neque et provident aspernatur. Incidunt iusto beatae illo minus vel. Quis sint sunt et facilis doloribus eligendi error est. Ipsum similique.
...
```

## Submit your work

Each student must submit this assignment individually. Use Visual Studio Code to perform git `stage`, `commit` and `push` actions to submit. These actions are all available as menu items in Visual Studio Code's Source Control panel.

1. Type a short note about what you have done to the files in the `Message` area, and then type `Command-Enter` (Mac) or `Control-Enter` (Windows) to perform git `stage` and `commit` actions.
1. Click the `...` icon next to the words, "Source Control" and select "Push" to perform the git `push` action. This will upload your work to your repository on GitHub.com.

Be sure to include the following:

- The original plain text data file which you downloaded from the Internet before it was modified by your Python program. Place this within the `data` directory.
- Your Python program which you wrote to "scrub" the data in the file named `munge.py`.
- The Excel or other formatted spreadsheet file containing the "clean" data and the formulas with the analysis you performed.
- your report in the file named [README.md](./README.md).

![Pushing work in Visual Studio Code](./images/vscode_stage_commit_push.png)
