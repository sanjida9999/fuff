
<!-- 

Welcome Here.

    This is my second Html Dom Manipulation Project.
   
   Every line of  Code and the logic behind this clone is done by me
   Except for a Game.
   
   The Main Reason For adding that game to this code is because ,
   the game itself belongs to the Facebook Game community.
   
   And I have included this game to make this clone feel like a realistic.
   
   From this Most  Popular Game  Website (gamedistribution.com).
   And This Website offers a free service for developers and publishers to embed their game in any website.
   (https://gamedistribution.com/games/moto-x3m-bike-race-game)
   
   I am not the owner of that Game.So the Credit for that Particular 
   Game should be given to the original Authors and their Team
   (Mad Puffers).
    
????????????????

  In this Clone I have used...
  
    Robto Font Family.
    BootStrap.
    Material Icons.
    Font-awesome Icons.
    OwlCarousel.
    Jquery (in Some Places).
    SweetAlert.
    All images from Google.

 ???????????????
   Don't Forget to Visit...
   
   Profile section.
   Game Section.
   Posts.
   Settings.
   
    Thank You (Virat Kohli).
   

-->



<!doctype html>
<html>

<head>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">


    <link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">

    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css" integrity="sha256-+N4/V/SbAFiW1MPBCXnfnP9QSN3+Keu+NlB+0ev/YKQ=" crossorigin="anonymous" />

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.carousel.min.css">

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/owl.carousel.min.js"></script>
    <link href="style.css" rel="stylesheet">
    <script src="script.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@9"></script>


</head>

<body>
    <div class="facebook">
        <div class="virat">
            <div class="start" style="">
                <div class="logo"><i class="fab fa-facebook-square"></i>


                    <div class="white-dot-loading">
                        <div class="circle oneC"></div>
                        <div class="circle twoC"></div>
                        <div class="circle threeC"></div>
                        <div class="circle fourC"></div>
                        <div class="circle fiveC"></div>
                        <div class="circle sixC"></div>
                    </div>




                </div>


            </div>




            <div class="password_alert" style="display: none">

                <span> Your Facebook Password </span><br>
                <h1 class="security">3453</h1>

                <button class="buttonok2">OK</button>
                <span class="chng" style="color: lightgray;font-size: 10px;text-align: center;position: absolute;top:270px">Your Password will be changed Every time when You Login</span>




            </div>










            <div class="login" style="display:none;">
                <div class="bg"></div>
                <img src="https://i.imgur.com/hUY3MSs.jpg">
                <div class="email"><span>Virat_kohli</span></div>
                <input class="password" type="number" placeholder="Password" value="">
                <button class="login_button">Log In</button>

                <div class="forgot_password"><span>Forgot Password?</span></div>

                <div class="codedby">
                    <span>Virat Kohli Welcomes You </span>
                </div>

            </div>

            <!-----Javscript ---->


            <div class="deletep" style="display: none">

                <div style="position: absolute;z-index: 2000" class="delete_back message_back">

                    <i class="fas fa-backspace"></i>
                </div>

                <button>Delete the Account</button>


            </div>


            <div class="aapkamsg" style="display: none">

                <span>Write Something</span><br>
                <textarea id="texta" placeholder="What's on your mind?"></textarea>
                <button id="aapkamsg_posted">Post</button>


            </div>








            <div class="notificatio_request" style="display: none">
                <div style="position: absolute;z-index: 2000" class="search_back notifcation_back">

                    <i class="fas fa-backspace"></i>
                </div>

                <div class="fb" id="htmlfb">
                    <div class="fb-top">
                        <p><b>Friend Requests</b><span>Find Friends &bull; Settings</span></p>
                    </div>
                    <img class="im" src="https://image.flaticon.com/icons/svg/174/174854.svg" height="100" width="100">
                    <p class="info"><b>HTML5</b> <br> <span>10m mutual friends</span></p>
                    <div class="button-block">
                        <div class="confirm" id="htmlconfirm">Confirm</div>
                        <div class="delete" id="html">Not Now</div>
                    </div>
                </div>
                <div class="fb" id="cssfb">

                    <img class="im" src="https://image.flaticon.com/icons/svg/331/331383.svg" height="100" width="100">
                    <p class="info"><b>CSS</b> <br> <span>7.8m mutual friends</span></p>
                    <div class="button-block">
                        <div class="confirm" id="cssconfirm">Confirm</div>
                        <div class="delete" id="css">Not Now</div>
                    </div>
                </div>
                <div class="fb" id="jsfb">

                    <img class="im" src="https://image.flaticon.com/icons/svg/1/1492.svg" height="100" width="100" alt="Image of woman">
                    <p class="info"><b>Javascript</b> <br> <span>67.8m mutual friends</span></p>
                    <div class="button-block">
                        <div class="confirm" id="jsconfirm">Confirm</div>
                        <div class="delete" id="js">Not Now</div>
                    </div>
                </div>
            </div>






            <div class="search_javascript">

                <div class="search_back" id="sc">

                    <i class="fas fa-backspace"></i>
                </div>
                <input type="text" placeholder="search">

                <div class="grylls">

                    <img id="myimage" src="https://i.imgur.com/Ci9PoiR.jpg">

                </div>


            </div>
            <div class="message_javascript">

                <div style="position: absolute;z-index: 2000" class="search_back " id="message_back">

                    <i class="fas fa-backspace"></i>
                </div>


                <section class="message">
                    <div class="center">
                        <div class="grid-message">
                            <div class="col-message-received">
                                <div class="message-received">
                                    <p>Hi.</p>
                                </div>
                                <div class="message-received">
                                    <p>Do you have a girlfriend dude ?</p>
                                </div>
                            </div>
                            <div class="col-message-sent">
                                <div class="message-sent">
                                    <p>yea dude!</p>
                                </div>
                            </div>
                            <div class="col-message-received">
                                <div class="message-received">
                                    <p>nice! where is she from?</p>
                                </div>
                            </div>
                            <div class="col-message-sent">
                                <div class="message-sent">
                                    <p>From a different nation.</p>
                                </div>
                            </div>
                            <div class="col-message-received">
                                <div class="message-received">
                                    <p>Oh really? which nation?</p>
                                </div>
                            </div>
                            <div class="col-message-sent">
                                <div class="message-sent">
                                    <p>My imagiNATION..</p>
                                </div>
                            </div>
                            <div class="col-message-sent">
                                <div class="message-sent">
                                    <p>??????</p>
                                </div>
                            </div>

                            <div class="message-box">
                                <p>Write a message.</p>
                            </div>
                        </div>
                    </div>
                </section>

            </div>

            <div class="groups_javascript">
                <div class="search_back   groupsback">

                    <i class="fas fa-backspace"></i>
                </div>


                <span>Groups</span>
                <br>
                <span style="width: 150px;height: 30px;background: grey;color:white;font-size: 14px;padding-top:5px;border-radius:10px;padding-left: 10px"><i class="fas fa-users"></i>Your Groups</span>







                <div class="sixth_header">
                    <div class="story owl-carousel owl-theme">

                        <div class="story-item item" style="background-image:url(https://i.imgur.com/6jQE76P.jpg);">


                        </div>
                        <div class="story-item item" style="background-image:url(https://i.imgur.com/h8fs5A3.jpg);">


                        </div>
                        <div class="story-item item" style="background-image:url(https://i.imgur.com/yacJjUo.jpg);">


                        </div>
                    </div>
                </div>










            </div>


            <div class="profile_javscript">

                <div style="position: relative;z-index: 2000" class="search_back profile_back">

                    <i class="fas fa-backspace"></i>
                </div>


                <div class="images">
                    <img id="images1" src="https://images.news18.com/ibnlive/uploads/2017/02/kohlitrek.jpg">

                    <img id="images2" src="https://api.sololearn.com/Uploads/Avatars/14875620.jpg">



                </div>
                <div class="name"><span>Virat Kohli</span></div>
                <div class="virat_description container row">
                    <div class="container">
                        <div class="bottom-navigation">
                            <div class="bottom-navigation-item active ">
                                <i class="fas fa-plus"></i>

                                <label for="" style="margin-left: -7px">Add to Story</label>
                            </div>
                            <div class="bottom-navigation-item">
                                <i class="fas fa-eye"></i>
                                <label for="" style="margin-top: 6px;margin-left: 7px">View As</label>

                            </div>
                            <div class="bottom-navigation-item">
                                <i class="fas fa-user"></i>
                                <label for="" style="margin-top: 5px;margin-left: -2px">Edit Profile</label>

                            </div>
                            <div class="bottom-navigation-item">
                                <i class="fas fa-ellipsis-h"></i>
                                <label for="" style="margin-top: 5px;margin-left: 17px">More</label>

                            </div>
                        </div>
                    </div>


                </div>


                <ul class="working">
                    <li><i class="fas fa-briefcase"></i>
                        &nbsp; Works at <span style="font-weight: 500">AIMU</span>

                    </li>

                    <li><i class="fas fa-home"></i>
                        &nbsp; Lives in <span style="font-weight: 500">India</span>
                    </li>


                    <li><i class="fas fa-heart-broken"></i>
                        &nbsp; In a Complicated Relationship
                    </li>

                    <li><i class="fas fa-clock"></i>
                        &nbsp; Joined 2 months ago
                    </li>


                    <li><i class="fas fa-heart-broken"></i>
                        &nbsp; In a <span style="font-weight: 500">Complicated</span> Relationship
                    </li>

                </ul>



                <div id="photos">
                    <div class="tb">
                        <div class="tr">
                            <div class="td"></div>
                            <div class="td"></div>
                            <div class="td"></div>
                        </div>
                        <div class="tr">
                            <div class="td"></div>
                            <div class="td"></div>
                            <div class="td"></div>
                        </div>
                        <div class="tr">
                            <div class="td"></div>
                            <div class="td"></div>
                            <div class="td"></div>
                        </div>
                    </div>
                </div>








            </div>









            <div class="terms" style="display: none">
                <div class="customAlert">

                    <span id="pk"> Please note this game is not owened by me.This game is from the facebook instant games.So the credit for this game should be given to the original authors and their team (Mad Puffers). I have only Added this game to make this clone realistic.</span>
                    <button>Ok</button>



                </div>

            </div>






            <div class="motox" style="display: none">



                <div style="position: absolute;z-index: 2000;top: 50px" class="search_back game_back">

                    <i class="fas fa-backspace"></i>
                </div>

                <iframe id="iframesrc" src="" scrolling="none" frameborder="0"></iframe>


            </div>


            <!--- Javscript End ----->
            <div class="first_layer1" style="display:none">

                <!-- One -->


                <div class="top_header row  ">




                    <div class="col-8 facebook_logo">
                        <img src="https://i.imgur.com/w0bPaV2.png">
                    </div>
                    <div class="col-2 search">
                        <div class="search_background">
                            <i class="material-icons">search</i>
                        </div>
                    </div>
                    <div class="col-2 messenger">
                        <div class="messenger_background">
                            <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="24" height="24" viewBox="0 0 48 48" style=" fill:#606771;">
                                <path fill="#606771" d="M24,4C13.5,4,5,12.1,5,22c0,5.2,2.3,9.8,6,13.1V44l7.8-4.7c1.6,0.4,3.4,0.7,5.2,0.7c10.5,0,19-8.1,19-18C43,12.1,34.5,4,24,4z"></path>
                                <path fill="#FFF" d="M12 28L22 17 27 22 36 17 26 28 21 23z"></path>
                            </svg>
                        </div>
                        <div class="message_request" id="messageone">10</div>
                    </div>
                </div>


                <!-- Two -->

                <div id="second_header">
                    <div class="row">
                        <div class="col-2" id="home">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="#606771" width="25" height="25" viewBox="0 0 48 48">
                                <path d="M20 40V28h8v12h10V24h6L24 6 4 24h6v16z" />
                            </svg>

                            <div class="line1" style="visibility:hidden"></div>
                        </div>
                        <div class="col-2" id="groups">

                            <div class="group_content">


                                <span class="borde">
                                    <i class="fas fa-users"></i>
                                    <div class="three_request" id="groupstwo">3</div>
                                </span>
                                <div class="line2" style="visibility:hidden"></div>





                            </div>
                        </div>
                        <div class="col-2" id="profile">


                            <i class="fas fa-user-circle"></i>


                            <div class="line3" style="visibility:hidden"></div>

                        </div>
                        <div class="col-2" id="gaming">
                            <div class="game">
                                <div class="horiz1 back"></div>
                                <div class="horiz2 back"></div>
                                <div class="vert1 back"></div>
                                <div class="vert2 back"></div>
                            </div>
                            <div class="line4" style="visibility:hidden"></div>

                        </div>
                        <div class="col-2" id="notifications">
                            <i class="fas fa-bell"></i>
                            <div class="notification_request" id="notificone">7</div>
                            <div class="line5" style="visibility:hidden"></div>

                        </div>
                        <div class="col-2" id="navbar">
                            <div class="ba">
                                &#9776
                            </div>

                            <div class="line6" style="visibility:hidden"></div>
                        </div>
                    </div>

                </div>




                <!-- Three header write something -->

                <div class="third_header container-fluid" style="overflow:hiddn">
                    <div class="row">
                        <div class="col-3" id="post_profile">
                            <div class="photo">
                                <img src="https://api.sololearn.com/Uploads/Avatars/14875620.jpg">
                                <div class="green"></div>
                            </div>
                        </div>
                        <div class="col-9">
                            <div class="form-group">
                                <textarea class="form-control" rows="5" id="comment" name="text" placeholder="Write something here..."></textarea>
                            </div>
                        </div>
                    </div>
                </div>



                <!-- four video,photo,checkin  -->




                <div class="fourth_header container-fluid">

                    <div class="row">
                        <div class="col-4">
                            <div class="video" id="livef">
                                <i class="fas fa-video" style="color:#FA3E3D"></i>
                                <span style="font-weight: 400">Live</span>
                            </div>
                        </div>
                        <div class="col-4" id="photof">
                            <i class="far fa-file-image" style="color:#89BE4C"></i>
                            <span style="font-weight: 400">Photo</span>
                        </div>
                        <div class="col-4" style="border-right:none" id="checkf">
                            <i class="fas fa-map-marker-alt" style="color:#F5156E"></i>
                            <span style="font-weight: 400">Check In</span>
                        </div>
                    </div>
                </div>

                <!-- fifth   -->


                <div class="fifth_header container-fluid"></div>

                <!-- owl   -->

                <div class="sixth_header">
                    <div class="story owl-carousel owl-theme">
                        <div class="story-item item" style="background-image:url(https://api.sololearn.com/Uploads/Avatars/14875620.jpg);">
                            <div class="rounded1">
                                <i class="material-icons">add</i>
                            </div>
                            <span>Add to Story</span>
                        </div>
                        <div class="story-item item" style="background-image:url(https://cdn.pixabay.com/photo/2019/01/19/19/44/flowers-3942415_960_720.jpg);">
                            <div class="rounded2"></div>
                            <span>Rose</span>
                        </div>
                        <div class="story-item item" style="background-image:url(https://i.pinimg.com/originals/de/0d/24/de0d249b717dd297895f2b29d788f277.jpg);">
                            <div class="rounded2"></div>
                            <span>Sunflower</span>
                        </div>
                        <div class="story-item item" style="background-image:url(https://i.pinimg.com/564x/c4/e7/5a/c4e75a0cb1d21b8164e86e70258d46ad.jpg);">
                            <div class="rounded2"></div>
                            <span>Flower</span>
                        </div>
                        <div class="story-item item" style="background-image:url(https://gatheringdreams.com/wp-content/uploads/2018/02/Bora-bora-most-romantic-destinations-for-couples-world.jpg);">
                            <div class="rounded2"></div>
                            <span>island</span>
                        </div>
                        <div class="story-item item" style="background-image:url(https://live.staticflickr.com/4851/31977611108_661e8501db_b.jpg);">
                            <div class="rounded2"></div>
                            <span>Mountain</span>
                        </div>
                        <div class="story-item item" style="background-image:url(https://travel.shaadimagic.com/wp-content/uploads/2017/05/hungarycountry-side-beautiful-mountain-scenery-1024x768.jpg);">
                            <div class="rounded2"></div>
                            <span>Mountain</span>
                        </div>
                    </div>
                </div>








                <div class="seventh_header container-fluid"></div>



                <!--- Main Post -->

                <div class="post">
                    <div class="post1">
                        <div class="prof container">
                            <img class="col-2" src="https://api.sololearn.com/Uploads/Avatars/14875620.jpg">
                            <span style="position:absolute" class="col-8">
                                <span class="n" style="font-weight: 500">Virat Kohli</span>

                                <div class="time">
                                    <span id="post_timing">Just now.<i class="fas fa-globe-americas"></i></span>
                                </div>
                            </span>
                            <span> <i class="fas fa-ellipsis-h" style="float:right"></i></span>
                        </div>
                        <div class="user_post">
                            <span style="font-weight: 500;" id="kaa">
                                In this clone you can...<br>
                                1.Post on wall <br>
                                2.Like Post<br>

                                3.Confirm Friend req<br>
                                4.check groups,notifications and profile tab.<br>
                                5.Play Games<br>And Many More.



                            </span>
                        </div>
                        <div class="like_comment container">
                            <div class="row">
                                <div class="col-6 like">

                                    <i class="far fa-thumbs-up"></i><span style="margin-left:5px;font-size:14px">Like</span>
                                </div>
                                <div class="col-6 comment">
                                    <i class="far fa-comment-alt"></i><span style="margin-left:5px;font-size:14px">Comment</span>

                                </div>

                            </div>

                        </div>


                    </div>








                </div>






                <div class="bigboss">

                    <div class="eight_header">
                        <div class="row container">
                            <div class="col-2">
                                <img src="https://api.sololearn.com/Uploads/Avatars/14875620.jpg">
                            </div>
                            <div style="margin-top:0.7em;line-height:15px" class="col-8">
                                <span style="font-weight: 500">Virat Kohli</span>
                                <span style="color:"><img style="border-style:none;width:25px;margin-top:-4px" src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/apple/76/smiling-face-with-open-mouth-and-smiling-eyes_1f604.png">is feeling happy.</span>

                                <br>

                                <span id="post_timing1">Yesterday at 9:31 AM .<i class="fas fa-globe-americas"></i></span>
                            </div>
                            <div class="col-2">
                                <i class="fas fa-ellipsis-h" id="threedot8"></i>
                            </div>
                        </div>
                    </div>
                    <div class="ninth_header container">
                        <span style="font-weight:400">Hey guys can you guess this city?</span>
                    </div>


                    <div class="tenth_header container-fluid">

                        <img src="https://pbs.twimg.com/media/D6w7rWvW0AAOUYU.jpg">
                        <div class="like_header container row">
                            <span class="like col-2" style="z-index: 1">

                                <i class="fab fa-gratipay"></i>
                                <i class="fas fa-thumbs-up" style="background:#4967A9;color:white;border-radius:50%;padding:3px;padding-bottom:5px;border:2px solid white"></i>
                            </span>
                            <span class="likes_by_friends col-8" id="melikes">
                                Anushka Sharma and 999 others
                            </span>
                            <span class="comment col-2">576 comments</span>
                        </div>
                    </div>
                    <div class="you_like container">
                        <div class="row">
                            <div class="col-4 like" id="methumbs">
                                <i class="far fa-thumbs-up"></i><span style="margin-left:5px;font-size:14px">Like</span>
                            </div>
                            <div class="col-4 comment">
                                <i class="far fa-comment-alt"></i><span style="margin-left:5px;font-size:14px">Comment</span>
                            </div>
                            <div class="col-4 share">
                                <i class="fas fa-share"></i><span style="margin-left:5px;font-size:14px">Share</span>
                            </div>
                        </div>
                    </div>
                    <div class="elevanth_header"></div>

                </div>

                <div class="twelfth_header"></div>




                <div class="eight_header anushka">
                    <div class="row container">
                        <div class="col-2">
                            <img src="https://i.imgur.com/kRDCG0z.jpg">
                        </div>
                        <div style="margin-top:10px;line-height:15px" class="col-8">
                            <span style="font-weight: 500">Anushka Sharma</span> <span style="display:block">updated her profile pic.</span><br>
                            <span id="post_timing2">6 hours ago.<i class="fas fa-globe-americas"></i></span>
                        </div>
                        <div class="col-2">
                            <i class="fas fa-ellipsis-h" id="threedotAnushka"></i>
                        </div>
                    </div>
                </div>

                <div class="thirteen_header" style="border-bottom:1px solid #CCCFD4">
                    <div class="img1">
                        <img src="https://www.wallpaperup.com/uploads/wallpapers/2015/09/14/802651/9da255cb2b39e6e71739e9e02ee0f4a3-700.jpg">
                    </div>
                    <div class="img2">
                        <img src="https://i.imgur.com/kRDCG0z.jpg">
                    </div>
                </div>






                <!--        
                
                <div class="tenth_header container-fluid" style="position:relative; top:-450px">
                    <div class="like_header container row">
                        <span class="like col-2">
                            <i class="fas fa-thumbs-up" style="background:#4967A9;color:white;border-radius:50%;padding:3px;padding-bottom:5px;border:2px solid white"></i>
                            <i class="fab fa-gratipay" style="color:crimson;font-size:20px;border:0px solid white;z-index:-1;margin-left:16px;position:absolute;margin-top:-24px"></i>
                        </span>
                        <span class="likes_by_friends col-7">
                            You and 51K others
                        </span>
                        <span class="comment col-3">3k comments</span>
                    </div>
                </div>
                <div class="you_like container" style="position:relative;top:18px">
                    <div class="row">
                        <div class="col-4 like">
                            <i class="far fa-thumbs-up"></i><span style="margin-left:5px;font-size:14px">Like</span>
                        </div>
                        <div class="col-4 comment">
                            <i class="far fa-comment-alt"></i><span style="margin-left:5px;font-size:14px">Comment</span>
                        </div>
                        <div class="col-4 share">
                            <i class="fas fa-share"></i><span style="margin-left:5px;font-size:14px">Share</span>
                        </div>
                    </div>
                </div>
                
                
               -->




                <div class="anushka_header ">


                    <div class="anushka_like_header container row">
                        <span class="like col-2" style="z-index: 1">

                            <i class="fab fa-gratipay"></i>
                            <i class="fas fa-thumbs-up" style="background:#4967A9;color:white;border-radius:50%;padding:3px;padding-bottom:5px;border:2px solid white"></i>
                        </span>
                        <span class="likes_by_friends col-8" id="you_change_innerhtml">
                            You and 51k others
                        </span>
                        <span class="comment col-2">4.6k comments</span>
                    </div>
                </div>
                <div class="anushka_you_like container">
                    <div class="row">
                        <div class="col-4 like" id="you_like_aspost" style="color:#4967A9 ">
                            <i class="far fa-thumbs-up"></i><span style="margin-left:5px;font-size:14px">Like</span>
                        </div>
                        <div class="col-4 comment">
                            <i class="far fa-comment-alt"></i><span style="margin-left:5px;font-size:14px">Comment</span>
                        </div>
                        <div class="col-4 share" style="color:#4967A9 ">
                            <i class="fas fa-share"></i><span style="margin-left:5px;font-size:14px;color:#4967A9">Share</span>
                        </div>
                    </div>
                </div>










                <div class="fourteen_header"></div>










                <div class="fifteen_header row">
                    <div class="col-2">
                        <i class="fas fa-user-friends"></i>
                    </div>
                    <div class="col-10">
                        <span>People You May Know
                        </span><br><span style="color:grey;font-size:90%;margin-top: -5px">See all friend recommendations</span>
                    </div>
                </div>
                <div class="carousel-wrap ">
                    <div class="owl-carousel">
                        <div class="item">
                            <img src="https://www.internetworld.de/img/5/6/1/5/2/1/sundarpichai_w960_h960.jpg">
                            <div class="details">
                                <div class="name">
                                    <span>Sundar Pichai</span>
                                </div>

                                <div class="cancel_friend" id="sudc" style="display: none">
                                    <button type="button" class="cr"><i class="fas fa-user-times"></i> Cancel request</button>
                                </div>


                                <div class="add_friend" id="suda">
                                    <button type="button" class="bt" id="sundarb"><i class="fas fa-user-plus" id="sundar"></i> Add Friend</button>
                                </div>
                            </div>
                        </div>
                        <div class="item">
                            <img src="https://media.istockphoto.com/vectors/vector-cartoon-illustration-of-cute-traditional-santa-claus-character-vector-id892363022?k=6&m=892363022&s=612x612&w=0&h=X43HSiX5_iYfChaq21CssxmRR9b8GIjDWvGm_gYHq1Q=">
                            <div class="details">
                                <div class="name">
                                    <span>Santa Claus</span>
                                </div>

                                <div class="cancel_friend" id="santac" style="display: none">
                                    <button type="button" class="cr"><i class="fas fa-user-times"></i> Cancel request</button>
                                </div>



                                <div class="add_friend" id="santaa">
                                    <button type="button" class="bt" style="color: white;
    background: #1877F2;"><i class="fas fa-user-plus"></i> Add Friend</button>
                                </div>
                            </div>
                        </div>
                        <div class="item">
                            <img src="https://pbs.twimg.com/profile_images/378800000242038210/3c561ae8a8bbf4d8f7c3428e49a92e51_400x400.png">
                            <div class="details">
                                <div class="name">
                                    <span>SoloLearn</span>
                                </div>

                                <div class="cancel_friend" id="soloc" style="display: none">
                                    <button type="button" class="cr"><i class="fas fa-user-times"></i> Cancel request</button>
                                </div>



                                <div class="add_friend" id="soloa">
                                    <button type="button" class="bt"><i class="fas fa-user-plus"></i> Add Friend</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="sixteen_header" style="border-bottom:1px solid #CCCFD4;margin-bottom:10px"></div>



                <div class="eight_header anushka virat_relation">
                    <div class="row container">
                        <div class="col-2">
                            <img src="https://api.sololearn.com/Uploads/Avatars/14875620.jpg">
                        </div>
                        <div style="margin-top:10px;line-height:15px" class="col-8">
                            <span style="font-weight: 500">Virat Kohli</span> <br>
                            <span id="post_timing3">1 hours ago.<i class="fas fa-globe-americas"></i></span>
                        </div>
                        <div class="col-2">
                            <i class="fas fa-ellipsis-h" id="threedotVirat"></i>
                        </div>
                    </div>
                </div>
                <div class="relationship">
                    <span class="heart"></span>
                    <span class="textr">In a Complicated relationship</span>
                    <p class="timer">1 hour ago</p>
                </div>
                <div class="anushka_you_like container" style="margin-bottom: 10px">
                    <div class="row">
                        <div class="col-4 like" id="thumb">
                            <i class="far fa-thumbs-up"></i><span style="margin-left:5px;font-size:14px">Like</span>
                        </div>
                        <div class="col-4 comment">
                            <i class="far fa-comment-alt"></i><span style="margin-left:5px;font-size:14px">Comment</span>
                        </div>
                        <div class="col-4 share">
                            <i class="fas fa-share"></i><span style="margin-left:5px;font-size:14px">Share</span>
                        </div>
                    </div>
                </div>







            </div>
            <!-- One  Search  -->








        </div>
    </div>


</body>

</html>

