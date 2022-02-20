import csv
import os

# Finding relative directory for files
direct = (os.path.dirname(__file__)) + "\data"
rows = []
list1= []
def sectionprint(list1d):
        print(list1d)
        f = open('mess.html','a')
        add = "shop name1"
        body ="""
                <!-- Slide -->
                                    <div class="swiper-slide">
                                        <!-- Testimonials -->
                                            <div class="cards-2">
                                                <div class="container">
                                                    <div class="row">
                                                        <div class="col-lg-12">
                                                            <h2>"""+list1d[0]+"""</h2>
                                                        </div> <!-- end of col -->
                                                    </div> <!-- end of row -->
                                                    <div class="row">
                                                        <div class="col-lg-12">

                                                            <!-- Card -->
                                                            <div class="card">
                                                                <div class="card-image">
                                                                    <h4>Breakfast</h4>
                                                                    <hr class="testimonial-line">
                                                                </div>
                                                                <div class="card-body">
                                                                    <div class="testimonial-text">"""+list1d[1]+"""</div>
                                                                </div>
                                                            </div>
                                                            <!-- end of card -->

                                                            <!-- Card -->
                                                            <div class="card">
                                                                <div class="card-image">
                                                                    <h4>Lunch</h4>
                                                                    <hr class="testimonial-line">
                                                                </div>
                                                                <div class="card-body">
                                                                    <div class="testimonial-text">"""+list1d[2]+"""</div>
                                                                </div>
                                                            </div>
                                                            <!-- end of card -->

                                                            <!-- Card -->
                                                            <div class="card">
                                                                <div class="card-image">
                                                                        <h4>Tea</h4>
                                                                    <hr class="testimonial-line">
                                                                </div>
                                                                <div class="card-body">
                                                                    <div class="testimonial-text">"""+list1d[3]+"""</div>
                                                                </div>
                                                            </div>
                                                            <!-- end of card -->

                                                            <!-- Card -->
                                                            <div class="card">
                                                                <div class="card-image">
                                                                        <h4>Dinner</h4>
                                                                    <hr class="testimonial-line">
                                                                </div>
                                                                <div class="card-body">
                                                                    <div class="testimonial-text">"""+list1d[4]+"""</div>
                                                                </div>
                                                            </div>
                                                            <!-- end of card -->

                                                        </div> <!-- end of col -->
                                                            </div> <!-- end of row -->
                                                </div> <!-- end of container -->
                                            </div> <!-- end of cards-2 -->
                                            <!-- end of testimonials -->
                                    </div>
                                    <!-- end of slide -->"""
        print("section made")
        f.write(body)
        f.close()


def headerprint():
    f = open('mess.html','w')
    add = "shop name1"
    head = """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                
                <!-- SEO Meta Tags -->
                <meta name="description" content="Sync is a landing page HTML template built with Bootstrap 4 for presenting mobile apps to the online audience and for getting visitors to become users.">
                <meta name="author" content="Siddhanth">

                <!-- OG Meta Tags to improve the way the post looks when you share the page on LinkedIn, Facebook, Google+ -->
                <meta property="og:site_name" content="" /> <!-- website name -->
                <meta property="og:site" content="" /> <!-- website link -->
                <meta property="og:title" content=""/> <!-- title shown in the actual shared post -->
                <meta property="og:description" content="" /> <!-- description shown in the actual shared post -->
                <meta property="og:image" content="" /> <!-- image link, make sure it's jpg -->
                <meta property="og:url" content="" /> <!-- where do you want your post to link to -->
                <meta property="og:type" content="article" />

                <!-- Webpage Title -->
                <title>AppName</title>
                
                <!-- Styles -->
                <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700&display=swap&subset=latin-ext" rel="stylesheet">
                <link href="css/bootstrap.css" rel="stylesheet">
                <link href="css/fontawesome-all.css" rel="stylesheet">
                <link href="css/swiper.css" rel="stylesheet">
                <link href="css/magnific-popup.css" rel="stylesheet">
                <link href="css/styles.css" rel="stylesheet">
                
                <!-- Favicon  -->
                <link rel="icon" href="images/favicon.png">
            </head>
            <body data-spy="scroll" data-target=".fixed-top">
                
                <!-- Preloader -->
                <div class="spinner-wrapper">
                    <div class="spinner">
                        <div class="bounce1"></div>
                        <div class="bounce2"></div>
                        <div class="bounce3"></div>
                    </div>
                </div>
                <!-- end of preloader -->
                

                <!-- Navigation -->
                <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
                    <div class="container">
                        <!-- Text Logo - Use this if you don't have a graphic logo -->
                        <!-- <a class="navbar-brand logo-text page-scroll" href="index.html">Sync</a> -->

                        <!-- Image Logo -->
                        <a class="navbar-brand logo-image" href="index.html"><img src="images/logo.svg" alt="alternative"></a> 
                        
                        <!-- Mobile Menu Toggle Button -->
                        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-awesome fas fa-bars"></span>
                            <span class="navbar-toggler-awesome fas fa-times"></span>
                        </button>
                        <!-- end of mobile menu toggle button -->

                        <div class="collapse navbar-collapse" id="navbarsExampleDefault">
                            <ul class="navbar-nav ml-auto">
                                <li class="nav-item">
                                    <a class="nav-link page-scroll" href="#description">MESS MENU <span class="sr-only">(current)</span></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link page-scroll" href="#features">SHOPS</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link page-scroll" href="#screens">LINKS</a>
                                </li>

                                <!-- Dropdown Menu -->          
                                <li class="nav-item dropdown">
                                    <a class="nav-link dropdown-toggle page-scroll" id="navbarDropdown" role="button" aria-haspopup="true" aria-expanded="false">TEAM</a>
                                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                                        <a class="dropdown-item" href="team.html"><span class="item-text">Siddhanth Bhat</span></a>
                                        <!--div class="dropdown-divider"></div> -->
                                    </div>
                                </li>
                                <!-- end of dropdown menu -->
                            </ul>
                            <span class="nav-item">
                                <a class="btn-outline-sm page-scroll" href="#download">DOWNLOAD</a>
                            </span>
                        </div>
                    </div> <!-- end of container -->
                </nav> <!-- end of navbar -->
                <!-- end of navigation -->

                
                    <!-- Slider Wrapper -->
                    <div id="screens" class="slider">
                        <div class="container">
                            <div class="row">
                                <div class="col-lg-12">
                                    
                                    <!-- Image Slider -->
                                    <div class="slider-container">
                                        <div class="swiper-container image-slider">
                                            <div class="swiper-wrapper">"""

    print("head made")
    f.write(head)
    f.close()


def footerprint():
        f = open('mess.html','a')
        add = "shop name1"
        foot= """
                                                                                

                                            </div> <!-- end of swiper-wrapper -->
                
                                            <!-- Add Arrows -->
                                            <div class="swiper-button-next"></div>
                                            <div class="swiper-button-prev"></div>
                                            <!-- end of add arrows -->
                
                                        </div> <!-- end of swiper-container -->
                                    </div> <!-- end of slider-container -->
                                    <!-- end of image slider -->
                
                                </div> <!-- end of col -->
                            </div> <!-- end of row -->
                        </div> <!-- end of container -->
                    </div> <!-- end of slider -->
                    <!-- end of Slider Wrapper -->





                <!-- Footer -->
                <div class="footer">
                    <div class="container">
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="footer-col first">
                                    <h5>About Sync</h5>
                                    <p class="p-small">Sync is a landing page HTML template built with Bootstrap 4 for presenting mobile apps</p>
                                </div> <!-- end of footer-col -->
                                <div class="footer-col second">
                                    <h5>Contact Info</h5>
                                    <ul class="list-unstyled li-space-lg p-small">
                                        <li class="media">
                                            <i class="fas fa-map-marker-alt"></i>
                                            <div class="media-body">22 Innovation Street, CA, US</div>
                                        </li>
                                        <li class="media">
                                            <i class="fas fa-envelope"></i>
                                            <div class="media-body"><a href="#your-link">office@syncmobile.com</a></div>
                                        </li>
                                        <li class="media">
                                            <i class="fas fa-phone-alt"></i>
                                            <div class="media-body"><a href="#your-link">+44 376 945 23</a></div>
                                        </li>
                                    </ul>
                                </div> <!-- end of footer-col -->
                                <div class="footer-col third">
                                    <h5>Value Links</h5>
                                    <ul class="list-unstyled li-space-lg p-small">
                                        <li><a href="terms-conditions.html">Terms & Conditions</a></li>
                                        <li><a href="privacy-policy.html">Privacy Policy</a></li>
                                        <li><a href="article-details.html">Article Details</a></li>
                                    </ul>
                                </div> <!-- end of footer-col -->
                                <div class="footer-col fourth">
                                    <h5>Other Apps</h5>
                                    <ul class="list-unstyled li-space-lg p-small">
                                        <li><a href="#your-link">Scientific Calculator</a></li>
                                        <li><a href="#your-link">Advanced Timer</a></li>
                                        <li><a href="#your-link">Music Store</a></li>
                                    </ul>
                                </div> <!-- end of footer-col -->
                                <div class="footer-col fifth">
                                    <span class="fa-stack">
                                        <a href="#your-link">
                                            <i class="fas fa-circle fa-stack-2x"></i>
                                            <i class="fab fa-facebook-f fa-stack-1x"></i>
                                        </a>
                                    </span>
                                    <span class="fa-stack">
                                        <a href="#your-link">
                                            <i class="fas fa-circle fa-stack-2x"></i>
                                            <i class="fab fa-twitter fa-stack-1x"></i>
                                        </a>
                                    </span>
                                    <span class="fa-stack">
                                        <a href="#your-link">
                                            <i class="fas fa-circle fa-stack-2x"></i>
                                            <i class="fab fa-pinterest-p fa-stack-1x"></i>
                                        </a>
                                    </span>
                                    <span class="fa-stack">
                                        <a href="#your-link">
                                            <i class="fas fa-circle fa-stack-2x"></i>
                                            <i class="fab fa-instagram fa-stack-1x"></i>
                                        </a>
                                    </span>
                                </div> <!-- end of footer-col -->
                            </div> <!-- end of col -->
                        </div> <!-- end of row -->
                    </div> <!-- end of container -->
                </div> <!-- end of footer -->  
                <!-- end of footer -->


                <!-- Copyright -->
                <div class="copyright">
                    <div class="container">
                        <div class="row">
                            <div class="col-lg-12">
                                <p class="p-small">Copyright © 2020 <a href="https://inovatik.com">Inovatik</a> - All rights reserved</p>
                            </div> <!-- end of col -->
                        </div> <!-- enf of row -->
                    </div> <!-- end of container -->
                </div> <!-- end of copyright --> 
                <!-- end of copyright -->
                
                    
                <!-- Scripts -->
                <script src="js/jquery.min.js"></script> <!-- jQuery for Bootstrap's JavaScript plugins -->
                <script src="js/popper.min.js"></script> <!-- Popper tooltip library for Bootstrap -->
                <script src="js/bootstrap.min.js"></script> <!-- Bootstrap framework -->
                <script src="js/jquery.easing.min.js"></script> <!-- jQuery Easing for smooth scrolling between anchors -->
                <script src="js/swiper.min.js"></script> <!-- Swiper for image and text sliders -->
                <script src="js/jquery.magnific-popup.js"></script> <!-- Magnific Popup for lightboxes -->
                <script src="js/validator.min.js"></script> <!-- Validator.js - Bootstrap plugin that validates forms -->
                <script src="js/scripts.js"></script> <!-- Custom scripts -->
            </body>
            </html>"""
        print("foot made")
        f.write(foot)
        f.close()

def generatelist():
    filename = ".\data\mess.csv" #PATH OF EMPLOYEE LIST
    # initializing the titles and Emprows list
    global list1
    global rows

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        
        # extracting field names through first row
        row = next(csvreader)
    
        # extracting each data row one by one
        for row in csvreader:
            list1.append(row)

            
def main():
    headerprint()
    generatelist()
    global list1
    #list1d=["null"]*10
    #print(list1d)
    for i in range(len(list1)):
           list1d=list1[i]
           sectionprint(list1d)
    footerprint()

if __name__=="__main__":
    main()
exit()