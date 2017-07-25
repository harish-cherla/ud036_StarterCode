import webbrowser
import os


def open_movies_page(moviesList):
    """Compose and render the web page"""
    #Get Template
    viewPath = os.getcwd()+"/template.tpl"
    fileContent  = open(viewPath,'r')
    fileContent = fileContent.read()

    #compose dynamic view
    viewContent=""
    for movie in moviesList:
        viewContent = viewContent + '''<div class="col-lg-4">
              <a href="javascript:void(0)" onclick="javascript:loadVideo(\''''+ movie.trailer +'''\')" ><img class="img img-thumbnail" src="'''+ movie.poster +'''" alt="Generic placeholder image" width="250" height="250"></a>
              <h2>'''+ movie.title +'''</h2>
              <p>'''+ movie.story +'''</p>
              <p><a class="btn btn-default" href="javascript:void(0)" onclick="javascript:loadVideo(\''''+ movie.trailer +'''\')" role="button">View Trailer</a></p>
            </div>'''

    #Compose web page
    fileContent = fileContent.replace("{{View}}", viewContent)
        
    view = open(os.getcwd()+"/trailer.html",'w')
    view.write(fileContent)
    view.close()

    #render in the browser
    webbrowser.open(os.getcwd()+"/trailer.html")

    #EOF
