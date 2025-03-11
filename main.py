from fastapi import FastAPI
from pydantic import BaseModel

import sqlite3 as sql3
import pandas as pd


# Connect to ccle db
database = "ccle.sqlite"
conn = sql3.connect(database)

print('Creating API endpoints')
# Create the API app
app = FastAPI()

# Data models to handle request
class tcgaHotspot(BaseModel):
    gene: str
    cell_line: str

class hotspotGenes(BaseModel):
    cell_line: str

class hotspotCellline(BaseModel):
    gene: str

# Path operations and functions
@app.get("/tcga_hotspot/")
async def getTcgaHotspot(item: tcgaHotspot):
    # query ccle table
    Entrez_Gene_Id = item.gene
    DepMap_ID = item.cell_line
    query = f"""
        select *
        from ccle
        where Entrez_Gene_Id = '{Entrez_Gene_Id}' and DepMap_ID = '{DepMap_ID}'
    """
    result = pd.read_sql(query, conn)
    result = result.drop(columns=["index"])
    
    return result.to_dict('records')


@app.get("/hotspot_genes/")
async def getHotspotGenes(item: hotspotGenes, page: int = 1, page_size: int = 5):
    # pagination
    start = (page - 1) * page_size
    end = start + page_size
    
    # query ccle table 
    DepMap_ID = item.cell_line
    query = f"""
        select Entrez_Gene_Id
        from ccle
        where DepMap_ID = '{DepMap_ID}' and isTCGAhotspot = 1
    """
    result = pd.read_sql(query, conn).to_dict('records')
    
    return result[start:end]


@app.get("/hotspot_cell_line/")
async def getHotspotCellline(item: hotspotCellline, page: int = 1, page_size: int = 5):
    # pagination
    start = (page - 1) * page_size
    end = start + page_size

    # query ccle table
    Entrez_Gene_Id = item.gene
    query = f"""
        select DepMap_ID
        from ccle
        where Entrez_Gene_Id = '{Entrez_Gene_Id}' and isTCGAhotspot = 1
    """
    result = pd.read_sql(query, conn).to_dict('records')

    return result[start:end]

