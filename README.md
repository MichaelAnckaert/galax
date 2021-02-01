# Galax - Static site generator for HTML and Gemini

Galax is a static site generator that generates output in both HTML and Gemini format. The source content is written in Markdown format. 

## Project goals

The goal of **Galax** is to allow you to easily generate a static site in both HTML and Gemini output formats (future versions might include more output formats). Content is Write Once and Galax will take care of reformatting your contents to match the output formats. The source content is in Markdown format. Templates can be written in Jinja2 format and are used to output all output formats. 

**Galax** is built to support fairly minimalistic websites. I don't intend to add much support / work arounds to deal with large amounts of static files or images. 

## Getting started

You can install **Galax** by running `pip install galax`. All interaction is done through the **galax** executable. 

To create a new static site, run the command **galax init** in an empty directory. This will create the necessary configuration files and scaffolding for a new static site. 

The contents of your site lives in the _contents_ directory. All markdown files in the _contents_ directory will be turned into general pages on your site. You'll also find a directory called _articles_ in your contents directory. 

The directory _articles_ contains your blog articles. The filename of your articles should start with the publication date of the article, for example *2021-02-01-my-first-article.md*. See **Conventions** below for information.

To build your static site, run `galax build` from the root directory of your site. This will build both HTML and Gemini output file in the _output_ directory. 

## Conventions

**Galax** uses a number of conventions to generate your static site. 

For **articles**, you _must_ prefix the article filename with the publication date of the article. This publication date can be used in your blog list template and articles are sorted in a descending order based on this timestamp. An example of an article filename is *2021-02-01-my-first-article.md*. The filename of the article is used in the URL path but has no special significance otherwise. 

The first line of the article contents must be the **article title** in a Markdown  header line: 

``` 
# My interesting article about a topic
```

This title will be used in the blog list page to link to the article itself. 
