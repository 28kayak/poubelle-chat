# Poubell Chat 
Poubell chat is a chat bot application that run on Line App.
This application will answer your question about how to throw away trash in Japan(somewhere in Saitama Pref).

## Technology 
Poubell Chat uses a number of open source projects to work properly: 

* [Python3] - as a programming language 
* [heroku] - as a cloud application platform
* [Apache Solr] - as a search-engine to search xml data
* [Line SDK for python] - line sdk allows to communicate with users 
* [ngrok] - ngrok secure introspectable tunnels to localhost webhook development tool and debugging tool.  

And of course Poubell Chat itself is open source with a [public repository][dill]
 on GitHub.
 
## Architecture

![architecture](https://github.com/28kayak/poubelle-chat/blob/master/img/architecture.png)  

## Installation 

- Install Python3 
- Install Apache Solr  
For Linux(Centos)  
See [install solr]  
For Mac OS  
you can download solr by using `brew` 
```bash
brew install solr
```

#### NOTE
Downloading by brew, solr's file directory will slightly different from building it from binary or source.  
We do not edit config file for this project yet.   
But, keep mind if you keep using solr for your own projects. 

- Run solr on your machine and Open your local-solr to public using ngrok 
```bash
# start solr 
solr start -p 8983
# create solr core named trash  
solr create_core -c trash
# open port 8983 via ngrok 
ngrok http 8983
```
- edit app.py   
edit the line below.  
replace `YOUR RANDOM NUMBER` with http url that ngrok gives you.  
```python
     response = requests.get('http://YOUR RANDOM NUMBER.ngrok.io/solr/trash/select', params=params)
```

- create solr schema 
```bash
pwd 
$`PATH TO DIR`/Poubelle/solr_schema
chmod 700 define_schema.sh #if you need 
./define_schema.sh  
```
make sure you have status code with `0`
- insert data to solr 
```bash
pwd 
$`PATH TO DIR`/Poubelle/data
chmod 700 manage_poubelle.sh #if you need
./poubelle_data_A.xml
```
make sure you have status code with `0`



 
 [//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/28kayak/poubelle-chat>
   [python3]: <https://www.python.org/download/releases/3.0/>
   [heroku]: <https://www.heroku.com/>
   [Apache Solr]: <http://lucene.apache.org/solr/>
   [Line SDK for python]: <https://github.com/line/line-bot-sdk-python>
   [ngrok]:<https://ngrok.com/>
   [install solr]:<https://github.com/28kayak/Centos_command_list/blob/master/install_apache_solr.md>