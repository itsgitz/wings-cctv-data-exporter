let exportButton = document.getElementById('exportButton')
let cctvDataArray = [];
let jsonData;

exportButton.onclick = function() {
  let tableData = document.getElementById('tableData')

  for (let i = 1; i < tableData.rows.length; i++) {
    let cctvName = tableData.rows.item(i).children[4].children[0].innerHTML;
    let getCurrentImage = tableData.rows.item(i).children[16].children[0].children[1]; 

    if (getCurrentImage) {
      getCurrentImage = getCurrentImage.currentSrc ? getCurrentImage.currentSrc : '';
    } else {
      getCurrentImage = '';
    }

    let imageFileName = getCurrentImage.split('/')[10]
    imageFileName = imageFileName ? imageFileName : '';

    cctvDataArray.push({
      name: cctvName,
      file: imageFileName
    });
  }

  jsonData = JSON.stringify(cctvDataArray)

  console.log(jsonData)
}
