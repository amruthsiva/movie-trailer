#!/usr/bin/env python
import webbrowser
import os
import re
print("Content-type:text/html \n")
main_page_head = '''
<!doctype html>
<html>
   <head>
      <meta name="viewport" content="width=device-width,initial-scale=1">
      <link rel="stylesheet" type="text/css" href="trailer.css">
      <center>
         <title>MOVIE TRAILERS</title>
      </center>
      <center>
         <h2>TRAILERS</h2>
      </center>
      <div id="myModal" class="modal">
         <div class="modal-content">
            <span class="close">&times;</span>
            <iframe width="100%" height="250" src="" frameborder="0"
             {movie_tiles} allow = "autoplay; encrypted-media"
             allowfullscreen></iframe>
         </div>
      </div>
      <script>
         var modal=document.getElementById('myModal');
         var span=document.getElementsByClassName("close")[0];
         onc=function (c){
             modal.style.display="block";
             document.getElementsByTagName("iframe")[0].setAttribute("src",
             'https://www.youtube.com/embed/'+c);
         }
         span.onclick=function(){
         modal.style.display="none";
         }
         window.onclick=function(event){
         if(event.target==modal){
         modal.style.display="none";
         }
         }
      </script>
   </head>
'''

main_page_content = '''
   <body>
      <div class="container">
         <div class="box light_blue" onclick="onc('6zB6wZKEObc')">
            <div class="background">
               <img vspace=25px;
                  src="https://bit.ly/2x4JgkO" alt="intime pic">
               <center>
                  <p>INTIME</p>
               </center>
            </div>
         </div>
         <div class="box red1" onclick="onc('yseqtsTfIl8')">
            <div class="background">
               <img vspace=25px;
                  src="https://bit.ly/2kb2LyV" alt="tod pic" >
               <center>
                  <p>Total Overdose</p>
               </center>
            </div>
         </div>
         <div class="box green" onclick="onc('K-5EdHZ0hBs')">
            <div class="background">
               <img vspace=25px;
                  src="https://bit.ly/2KIYvlz" alt="nfs pic" >
               <center>
                  <p>NFS 2</p>
               </center>
            </div>
         </div>
         <div class="box orange" onclick="onc('j-ZYwbJtQ9g')">
            <div class="background">
               <img vspace=25px;
                  src="https://bit.ly/2J0Tojk" alt="roadrash pic" >
               <center>
                  <p>Road Rash</p>
               </center>
            </div>
         </div>
         <div class="box white" onclick="onc('K0u_kAWLJOA')">
            <div class="background">
               <img vspace=25px;
                  src="https://bit.ly/2Iya969" alt="god of war pic" >
               <center>
                  <p>God Of War</p>
               </center>
            </div>
         </div>
         <div class="box black" onclick="onc('mNJMQtmWT14')">
            <div class="background">
               <img vspace=25px;
                  src="https://bit.ly/2x07vkp" alt="last day on earth pic">
               <center>
                  <p>Last Day On Earth</p>
               </center>
            </div>
         </div>
      </div>
   </body>
</html>
'''

movie_titles_content = '''
<div class="col-mod-6 col-lg-4 movie-title text-center"
        data-trailer-youtube-id="{trailer_youtube_id}"
        data-toggle="modal" data-target="#trailer">
        <img src="{poster_image_url}" width="220" height="#trailer">
        <h2 style="color:white;">{movie_title}</h2>
</div>
'''


def create_movie_titles_content(movies):
        content = ''
        a = "movie.trailer_youtube_url"
        b = "(?<=be/)[^&#]+"
        for movie in movies:
                # Extract the youtube.ID from the url
                youtube_id_match = re.search(r'(?<=v=)[^&#]+',
                                             a)
                youtube_id_match = youtube_id_match or re.search(r'b',
                                                                 a)
                trailer_youtube_id = (youtube_id_match.group(0)
                                      if youtube_id_match else None)
                # Append the title for the movie with its content filled in
                content += movie_titles_content.format(
                        movie_title=movie.title,
                        poster_image_url=movie.poster_image_url,
                        trailer_youtube_id=trailer_youtube_id)
                return content


def open_movie_page(movies):
        # Create or overwrite the output file
        output_file = open('fresh_tomatoes.html', 'w')

        # Replace the movie tiles placeholder generated content
        rendered_content = main_page_content.format(
                movie_tiles=create_movie_titles_content(movies))

        # Output the file
        output_file.write(main_page_head+rendered_content)
        output_file.close()

        # open the output file in the browser(in a new tab, if possible)
        url = os.path.abspath(output_file.name)
        webbrowser.open('file://' + url, new=2)
