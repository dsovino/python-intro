import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>DSs Favorites Movies EVER!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }        
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        /* BEGIN CUSTOM CSS */
          .movie_info {
          margin-top: 25px;
        }
        .movie-tile {
          min-height: 550px;
          padding: 30px;
        }
        .navbar-header {
          width: 100%;
          text-align: center;
        }

        .navbar.navbar-inverse.navbar-fixed-top {
          background-color: #0014FF !important;
          border-color: #FFFFFF;
          background-image: linear-gradient(to top,#FFFFFF 0,#020094 100%);
          height: 80px;
        }

        a.navbar-brand {
          color: #FFFFFF !important;
          font-size: 30px;
          text-shadow: 0 4px 5px rgba(0,0,0,.25) !important;
          margin: auto;
          width: 100%;
        }

        .container {
          padding-top: 15px;
        }

        .row {
          margin-bottom: 10px;
        }

        .left {
          width: 55px;
          position: relative;
          float: left;
        }

        .right {
          text-align: justify;
          position: relative;
          float: right;
          width: 80%;
        }

        i.fa {
          font-size: 25px;
          position: relative;
          color: red;
        }

        .fixed-bottom {
          background-color: #0014FF !important;
          border-color: #FFFFFF;
          background-image: linear-gradient(to bottom,#FFFFFF 3%,#020094 100%);
          height: 80px;
          position: fixed;
          bottom: 0px;
          right: 0;
          left: 0;
        }
        a.twit_link {
          top: 10px;
          font-size: 20px;
          color: white;
          /* margin-top: 10px; */
          position: relative;
          text-shadow: 0 4px 5px rgba(0,0,0,.25) !important;
        }

        i.fa.fa-twitter {
          color: white;
        }

        /* END CUSTOM CSS */
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">My Favorites Movies Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
    <div class="container">
      <div class="fixed-bottom">
        <div class="container">
          <div class="navbar-header">
            <a class="twit_link" href="https://twitter.com/dsovino" target="_blank"><i class="fa fa-twitter"></i>dsovino</a>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
    <div class="movie_info">
      <div class="row">
        <div class="left">
          <i class="fa fa-calendar-check-o"></i>
        </div>
        <div class="right">
          <span>{movie_year}</span>
        </div>
      </div>
      <div class="row">
        <div class="left">
          <i class="fa fa-film"></i>
        </div>
        <div class="right">
          <span>{movie_director}</span>
        </div>
      </div>
      <div class="row">
        <div class="left">
          <i class="fa fa-clock-o"></i>
        </div>
        <div class="right">
          <span>{movie_duration}</span>
        </div>
      </div>
      <div class="row">
        <div class="left">
          <i class="fa fa-info-circle"></i>
        </div>
        <div class="right">
          <span>{movie_storyline}</span>
        </div>
      </div>
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        # ADDED "storyline" in the output
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            movie_year=movie.year,
            movie_director=movie.director,
            movie_duration=movie.duration,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)