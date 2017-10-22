window.onload = function() {
        var rawFile = new XMLHttpRequest();
        var array=[];
        rawFile.open("GET", "2015photolist.txt", false);
        rawFile.onreadystatechange = function ()
        {
            if(rawFile.readyState === 4)
            {
                if(rawFile.status === 200 || rawFile.status == 0)
                {
                    var allText = rawFile.responseText;
                    array=allText.split("\n");
                }
            }
        }
        for(n=0; n<array.length; n++){
          file=array[n];
          var image=document.createElement("IMG");
          image.setAttribute("src",file+"");
          image.setAttribute("width", "300");
          image.setAttribute("height","200");
          document.getElementById("pics").appendChild(image);
        }
        rawFile.send(null);
    }