Zendesk-API
===================================

Scripts to GET content from a Zendesk Help Center instance. A separate text file is created for each JSON object (category, section, or article).

In this use case, a customer wanted to duplicate an existing Help Center for a new project. Zendesk [multibrand](https://support.zendesk.com/hc/en-us/articles/204108983) was prohibited.

- **get_article.py**: retrieve a single article
- **get_articles.py**: retrieve all articles
- **get_sections.py**: retrieve all sections

Prerequisites
--------------
* [Python 3.6](https://www.python.org/downloads/) with IDLE
* Zendesk subdomain with agent account and [API token](https://support.zendesk.com/hc/en-us/articles/226022787) (recommended)

Getting Started
---------------
Download the scripts and change the value for these variables as needed. Not all variables are used in all scripts:

- **articleID**: 	the Zendesk ID number of a given article
- **categoryID**: 	the Zendesk ID number of a given category
- **path**: 		the path to JSON text input/output files
- **pwd**: 			a Zendesk password (or API token)
- **sectionID**: 	the Zendesk ID number of a given section
- **subdomain**: 	target Zendesk instance
- **user** :		a Zendesk agent username (or username/token)

Execute the scripts using IDLE or another Python IDE.

Resources
---------------
- Zendesk [Help Center API docs](https://developer.zendesk.com/rest_api/docs/help_center/introduction) and
- [Backing up your knowledge base with the Zendesk API](https://help.zendesk.com/hc/en-us/articles/229136947)