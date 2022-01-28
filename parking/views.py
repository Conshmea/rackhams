from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import random

global FC_data

FC_data = 0

def info(request):
    global FC_data
    if request.method != "GET":
        return HttpResponse("NO")

    FC_ID = request.GET["id"]

    row = FC_data.index[FC_data['FC ID'] == FC_ID].tolist()

    row = int(row[0])

    FC_Name = str(FC_data.at[row,"FC Name"])

    FC_Status = str(FC_data.at[row,"Situation"])

    FC_Load = str(FC_data.at[row,"Tonnage"])

    FC_Owner = str(FC_data.at[row,"CMDR"])

    FC_Position = str(FC_data.at[row,"Position"])

    FC_Version = str(FC_data.at[row,"System"])

    response = FC_Name + "<br>"

    response += "ID: " + FC_ID + "<br>"

    response += "Owner: " + FC_Owner + "<br>"

    response += "Status: " + FC_Status + "<br>"

    response += "Position: " + FC_Position + "<br>"

    response += "Tonnage: " + FC_Load + "<br>"

    response += "Game Version: " + FC_Version + "<br>"

    
    
    return HttpResponse(response)















### START OF MAIN PAGE ###

def index(request):
    global FC_data
    carriers_at_P1 = 0
    carriers_at_P2 = 0
    carriers_at_P3 = 0
    carriers_at_P4 = 0
    carriers_at_P5 = 0
    carriers_at_P6 = 0
    carriers_at_N0 = 0
    carriers_at_N1 = 0
    carriers_at_N2 = 0
    carriers_at_N16 = 0
    carriers_on_ladder = 0

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('/var/peak-parking-8ba5d8f6a6f6.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key('1KX1FEFW7Kyk_Qc48qQRE7ubAogSQqTf4KrMwZp_egTo')
    sheet_instance = sheet.get_worksheet(0)
    FC_data = sheet_instance.get_all_records()
    FC_data = pd.DataFrame(data=FC_data)
       
    response = """<!DOCTYPE html>
<html>
<title>FC Chart</title>
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>

html {
  touch-action: none;
  white-space: nowrap;
  overflow-x: scroll;
}

body {
  background-size: 50px 50px;
  background-image:
  linear-gradient(to right, transparent 34px, grey 35px, transparent 1px),
  linear-gradient(to bottom, transparent 34px, grey 35px, transparent 1px);
  background-color: #000000;
  color: white;
}

.grid2 {
  display: grid;
  grid-template-columns: auto auto;
}

#N0 {
  position: absolute;
  left: 85px;
  top: 85px;
}

#N0-Title {
  position: absolute;
  left: 85px;
  top: 35px;
  color: #ffffff;
  text-align: center;
}

.planet {
  position:absolute;
  color: #ffffff;
}
</style>
<body>

<div id="N0-Title">
  <h3>N0 (peak)</h3>
</div>
<div id="N0">
  <img style="width:100px; height:100px;" src="http://ptns.space/assets/N0.png"></img>
</div>

<div style="left:220px; top:70px; color:white; position:absolute;" id="P1-Title">
  <h3>P1</h3>
</div>
<div style="left:210px; top:110px;" id="P1" class="planet">
  <img style="width:50px; height:50px;" src="http://ptns.space/assets/N0.png"></img>
</div>

<div style="left:320px; top:70px; color:white; position:absolute;" id="P1-Title">
  <h3>P2</h3>
</div>
<div style="left:310px; top:110px;" id="P1" class="planet">
  <img style="width:50px; height:50px;" src="http://ptns.space/assets/N0.png"></img>
</div>

<div style="left:420px; top:70px; color:white; position:absolute;" id="P1-Title">
  <h3>P3</h3>
</div>
<div style="left:410px; top:110px;" id="P1" class="planet">
  <img style="width:50px; height:50px;" src="http://ptns.space/assets/N0.png"></img>
</div>

<div style="left:520px; top:70px; color:white; position:absolute;" id="P1-Title">
  <h3>P4</h3>
</div>
<div style="left:510px; top:110px;" id="P1" class="planet">
  <img style="width:50px; height:50px;" src="http://ptns.space/assets/N0.png"></img>
</div>

<div style="left:620px; top:70px; color:white; position:absolute;" id="P1-Title">
  <h3>P5</h3>
</div>
<div style="left:610px; top:110px;" id="P1" class="planet">
  <img style="width:50px; height:50px;" src="http://ptns.space/assets/N0.png"></img>
</div>

<div style="left:720px; top:70px; color:white; position:absolute;" id="P1-Title">
  <h3>P6</h3>
</div>
<div style="left:710px; top:110px;" id="P1" class="planet">
  <img style="width:50px; height:50px;" src="http://ptns.space/assets/N0.png"></img>
</div>

<div style="left:920px; top:35px; color:white; position:absolute;" id="P1-Title">
  <h3>N1</h3>
</div>
<div style="left:885px; top:85px;" id="P1" class="planet">
  <img style="width:100px; height:100px;" src="http://ptns.space/assets/N0.png"></img>
</div>

<div style="left:1120px; top:35px; color:white; position:absolute;" id="P1-Title">
  <h3>N2</h3>
</div>
<div style="left:1085px; top:85px;" id="P1" class="planet">
  <img style="width:100px; height:100px;" src="http://ptns.space/assets/N0.png"></img>
</div>

<div style="left:1470px; top:35px; color:white; position:absolute;" id="P1-Title">
  <h3>N16 (Niaba)</h3>
</div>
<div style="left:1485px; top:85px;" id="P1" class="planet">
  <img style="width:100px; height:100px;" src="http://ptns.space/assets/N0.png"></img>
</div>

<div style="left:1295px; top:35px; color:white; position:absolute;" id="P1-Title">
  <h3>Ladder</h3>
</div>

<div style="left:1700px; top:1000px; color:white; position:absolute;">.</div>
"""

    response += "\n\n\n"

    for row in range(0,FC_data.index.stop):
        FC_Name = str(FC_data.at[row,"FC Name"]).upper()
        FC_ID = str(FC_data.at[row,"FC ID"]).upper()

        if FC_ID == "":
            FC_ID = FC_Name

        Tag = FC_ID.replace("-", "-<br>")

        body = str(FC_data.at[row,"Position"]).upper()

        if body == "N0" or body == "STAR":
            left = 100
            top = 200 + (carriers_at_N0 * 50)
            carriers_at_N0 = carriers_at_N0 + 1
        elif body == "P1":
            left = 200
            top = 175 + (carriers_at_P1 * 50)
            carriers_at_P1 = carriers_at_P1 + 1
        elif body == "P2":
            left = 300
            top = 175 + (carriers_at_P2 * 50)
            carriers_at_P2 = carriers_at_P2 + 1
        elif body == "P3":
            left = 400
            top = 175 + (carriers_at_P3 * 50)
            carriers_at_P3 = carriers_at_P3 + 1
        elif body == "P4":
            left = 500
            top = 175 + (carriers_at_P4 * 50)
            carriers_at_P4 = carriers_at_P4 + 1
        elif body == "P5":
            left = 600
            top = 175 + (carriers_at_P5 * 50)
            carriers_at_P5 = carriers_at_P5 + 1
        elif body == "P6":
            left = 700
            top = 175 + (carriers_at_P6 * 50)
            carriers_at_P6 = carriers_at_P6 + 1
        elif body == "N1":
            left = 900
            top = 200 + (carriers_at_N1 * 50)
            carriers_at_N1 = carriers_at_N1 + 1
        elif body == "N2":
            left = 1100
            top = 175 + (carriers_at_N2 * 50)
            carriers_at_N2 = carriers_at_N2 + 1
        elif body == "N16" or body == "NIABA":
            left = 1500
            top = 200 + (carriers_at_N16 * 50)
            carriers_at_N16 = carriers_at_N16 + 1
        else:
            left = 1300
            top = 85 + (carriers_on_ladder * 50)
            carriers_on_ladder = carriers_on_ladder + 1

        style = f"position: absolute; z-index: 9; hieght: 50px; width: 50px; left: {left}px; top: {top}px;"
        
        
        carrier_div =f"""<div style="{style}" id="{FC_ID}">
  <div onclick="load_data('{FC_ID}')" style="padding: 10px; cursor: pointer;" class="grid2" id="{FC_ID}drag">
    <img style="width:50px; height: 50px;" src="http://ptns.space/assets/carrier.png"></img>
    <h5>{Tag}</h5>
  </div>
</div>"""

        response += carrier_div

    response += "\n\n\n"

    response += """<div id="data_modal" class="w3-modal" style="z-index: 10">
    <div class="w3-modal-content w3-dark-grey">
      <div class="w3-container">
        <span onclick="document.getElementById('data_modal').style.display='none'" class="w3-button w3-display-topright">&times;</span>
        <p id="data_data_modal">Some text. Some text. Some text.</p>
        <br>
        <p style="cursor: pointer;" onclick="document.getElementById('data_modal').style.display='none'" >Close</p>
      </div>
    </div>
</div>
</body>
<script>
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    console.log(xmlHttp.responseText);
    return xmlHttp.responseText;
}

function load_data(FC_ID)
{
    var data = httpGet('http://ptns.space:8000/info?id='+FC_ID);
    document.getElementById('data_data_modal').innerHTML = data;
    document.getElementById('data_modal').style.display='block';
    
}

//const scrollContainer = document.querySelector("html");
//
//scrollContainer.addEventListener("wheel", (evt) => {
//    evt.preventDefault();
//    scrollContainer.scrollLeft += evt.deltaY;
//});
</script>
</html>"""
    
    
    return HttpResponse(response)


### END OF MAIN PAGE ###
