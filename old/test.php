<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>
    
    <head>
        <title>Cytoscape Web example</title>
       <script type="text/javascript"
       	src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.js"></script> 
        <!-- JSON support for IE (needed to use JS API) -->
        <script type="text/javascript" src="./js/min/json2.min.js"></script>
        
        <!-- Flash embedding utility (needed to embed Cytoscape Web) -->
        <script type="text/javascript" src="./js/min/AC_OETags.min.js"></script>
        
        <!-- Cytoscape Web JS API (needed to reference org.cytoscapeweb.Visualization) -->
        <script type="text/javascript" src="./js/min/cytoscapeweb.min.js"></script>
        
        <script type="text/javascript">
            window.onload=function() {
                // id of Cytoscape Web container div
                var div_id = "cytoscapeweb";
                
                // you could also use other formats (e.g. GraphML) or grab the network data via AJAX
                	$.ajax({   
                	        type: "GET",
                	        url: "<? echo $_GET['url']?>",       
                	        dataType:'text',   
                	        success: function(data, textStatus){
                
                // initialization options
                var options = {
                    // where you have the Cytoscape Web SWF
                    swfPath: "./swf/CytoscapeWeb",
                    // where you have the Flash installer SWF
                    flashInstallerPath: "./swf/playerProductInstall"
                };
                var visual_style = {
			edges:{
			width:{defaultValue:3,
			continuousMapper: { attrName: "weight", minValue: 3, maxValue: 10 }},
color: "#0B94B1"
			}

		}
                // init and draw
                var vis = new org.cytoscapeweb.Visualization(div_id, options);
                vis.draw({ network: data, visualStyle: visual_style });
            
                }
                                                                                              })


	};
        </script>
        
        <style>
            /* The Cytoscape Web container must have its dimensions set. */
            html, body { height: 100%; width: 100%; padding: 0; margin: 0; }
            #cytoscapeweb { width: 100%; height: 100%; }
        </style>
    </head>
    
    <body>
        <div id="cytoscapeweb">
            Cytoscape Web will replace the contents of this div with your graph.
        </div>
    </body>
    
</html>
