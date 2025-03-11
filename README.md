The Data Engineering Project Series (DEPS) showcases my expertise in designing and implementing data solutions that address practical challenges. Each project demonstrates proficiency with different technologies and methodologies in the data engineering field, highlighting my ability to build production-ready data pipelines. These independent projects reflect my approach to solving data problems, from initial architecture design to successful implementation. They represent my technical capabilities and problem-solving skills in data engineering.

> [!NOTE]
> The projects in DEPS are demonstration assignments originally created for technical interviews, designed to showcase technical skills and problem-solving capabilities.

# DEPS_002: TCGA Hotspot 

## Summary
This application creates an API endpoints to check for the following questions:
1. Determine whether a given gene and cell line is a TCGA hotspot.
2. List of TCGA hotspot genes for a given cell line.
3. List of cell lines that a given gene is a TCGA hotspot for.

## Tools
* Python
* Poetry
* FastAPI
* Sqlite3
* Pandas
* Docker

## What this application does
1. Download a csv file containing genes, cell lines, etc.
2. Get certain columns and 10000 rows from the file and insert data into a database.
3. Create API endpoints to answer the above 3 questions.

## How to run this application
1. Clone the repository.
2. Get inside the repository.
3. On the command line, run `docker compose up`
4. Application should now run at `http://0.0.0.0:8000`

## Endpoints Information
There are 3 endpoints for this application:
1. `/tcga_hotspot/`, which corresponds to question # 1.
2. `/hotspot_genes/`, which corresponds to question # 2.
3. `/hotspot_cell_line/`, which corresponds to question # 3.

## How to send a request to the API
Using an API platform of your choice (Insomnia, Postman, etc), decide which one of the 3 questions above you want to send a request for.
Request and response are in JSON format.

#### Question 1 (Determine whether a given gene and cell line is a TCGA hotspot):
![Example using gene: 7157 and cell line: ACH-000001](https://github.com/wiharto/DEPS_002/blob/main/images/istcgahotspot.png)

#### Question 2 (List of cell lines that a given gene is a TCGA hotspot for):
![Example using gene: 7157](https://github.com/wiharto/DEPS_002/blob/main/images/listofcelllines.png)

#### Question 3 (List of TCGA hotspot genes for a given cell line):
![Example using cell line: ACH-000007](https://github.com/wiharto/DEPS_002/blob/main/images/tcgahotspotgenes.png)
