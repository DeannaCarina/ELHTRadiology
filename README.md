
# ELHT Radiology Booking Service

## Contents
<ul>
    <li>
        <a href="#Introduction"><strong>Introduction</strong></a>
    </li>
    <li>
        <a href="#UX"><strong>UX</strong></a>               
    </li>
    <li>
        <a href="#Technologies"><strong>Technologies</strong></a>
    </li>
    <li>
        <a href="#Features"><strong>Features</strong></a>
    </li>
    <li>
        <a href="#Testing"><strong>Testing</strong></a>   
    </li>
    <li>
        <a href="#Deployment"><strong>Deployment</strong></a>
    </li>
    <li>
       <a href="#Credits"><strong>Credits</strong></a> 
    </li>
    <li>
        <a href="#Screenshots"><strong>Screenshots</strong></a>
    </li>
</ul>
<hr>

## Introduction

Portfolio Project Four: Full Stack Frameworks - Code Institute - Deadline 26th January 2022

This is my submission for Code Institute's (5P) Portfolio Project Four. It will be a progressive web application intended to make the work-flow and patient management easier within the radiology departments throughout East Lancashire Hospitals Trust. It will allow patients with radiology request froms (authorised by referring physicians) to book appointments within their preferred radiology location. The project will be deployed via Heroku to enable back-end functionality such as storing patient's confidential data within the PostgreSQL database and allowing the manipulation of this data. Members of staff will be able to log in as site administrators and manage bookings made by patients or add bookings themselves, this will be managed through Django's user authentication application. In the nearly 7 years I have worked at ELHT, we have never had a patient-lead booking system. As we are open-access at the majority of our hospital sites this means we cannot manage or predict our workflow meaning that at times during the work day we can be extremely busy, reducing the quality of patient care.

### Demo
A live of the website can be found <a href="https://elht-rbs.herokuapp.com/"><strong>HERE</strong></a><br>
<img src="readmeassets/responsive.png" width="600px">

## UX

As more people rely on accessing services online the role of UX design has become increasingly important in our digitized world. The five planes provide a conceptual framework for breaking down the task of designing experiences into component elements so that we can understand the problem as a whole. As this framework is structured, extensively used and consistently reliable, I have chosen to use the Five Planes method to design and implement my own website.

### Strategy

#### Vision

The ELHT Radiology Booking System (RBS) is a web-application providing patients with the ability to book their own radiology appointments. Currently within ELHT, the majority of our hospital sites are open-access for plain film radiography which can sometimes mean a long wait time for patients to be seen, however with a patient-lead booking system that limits the amount of patients that would attend, we could manage our workload, keep patients safe and manage their care more effectively due to having prior knowledge of the number of patients that would be attending. Other modalities within radiology do have a booking system, however this is lead by the booking team. By having a patient-lead booking system in place for these modalities, the booking team would get the majority of the information needed from the forms that the patient fills in online, rather than needing to contact the patient to get this information. More than 12 million appointments in primary care are not attended each year: this is about 6.5% of the appointments made (Family Practice, 2005). By having patients book their own appointments, it puts the onus on them to attend and put them in charge of their own care. In radiology, a huge amount of radiology referrals are never fulfilled - within East Lancashire, the current protocol is for a patient to see a referring physician who will in turn put a radiology request onto ICE (Integrated Clinical Environment), this request is then picked up by radiology who will queue the request for 4 weeks, if the patient does not attend for their examination within those for weeks then they are classed as a DNA (did not attend) and they must go back to the referring physician for a new request if they still require imaging. By giving patients the knowledge and opportunity to book themselves in for their examination, it will reduce the confusion that many patients have regarding our 'open-access' protocol, and encourage them to attend due to giving them the ability to book their own appointments. There will be individual booking forms for each modality (x-ray, CT, MRI, Ultrasound, Mammogram, others - which will consist of nuclear medicine, fluoroscopy and angiography) as each modality has their own safety questions that they must ask before the examination takes place. The website will also be an informative and educational tool for patients who are due to have a radiology examination. There are many patients who attend for radiation-based examinations who are very nervous about the radiation safety aspect of their examination and yet they choose not to ask the radiographer/technician for advice. By having this information on the website, patients can learn about radiation safety and make an informed decision about whether they truly need the examination or not.

#### Aims

<ol>
  <li>To allow the opportunity for patients to book and manage their own radiology appointments</li>
  <li>To give patients the opportunity to educate themselves on radiation safety prior to their visit</li>
  <li>To provide a simple to use contact form for site visitors to use in order to contact the radiology department</li>
  <li>To provide useful information to patients about radiology and the department to reduce 'white-coat-syndrome' and anxiety during their visit</li>
  <li>To give external companies the opportunity to partner with the radiology department and share their equipment prior to potential purchases</li>
  <li>To give radiology staff the opportunity to manage their workload and see in advance the patients they will encounter during the day</li>
</ol>

#### Target Audience(s)

<ol>
  <li>Patients who have been referred for radiology examinations by registered physicians</li>
  <li>External healthcare companies who have equipment to sell</li>
  <li>Radiology staff who want to have a more managable and predictable workload</li>
</ol>

#### User Stories

<ol>
  <li>As a Patient I can contact the radiology department so that I can discuss my radiology appointments/examinations</li>
  <li>As a patient I can use the IM service so that I can quickly contact the radiology department if needed</li>
  <li>As a patient I can use the X-RAY booking form so that I can book an x-ray appointment in ELHT</li>
  <li>As a patient I can use the CT booking form so that I can book a CT appointment in ELHT</li>
  <li>As a patient I can use the MRI booking form so that I can book an MRI appointment in ELHT</li>
  <li>As a patient I can use the Ultrasound booking form so that I can book an Ultrasound appointment in ELHT</li>
  <li>As a patient I can use the Mammogram booking form so that I can book a Mammogram appointment in ELHT</li>
  <li>As a patient I can use the Other Examination booking form so that I can book Nuclear Medicine, Fluoroscopy and Angiography appointments in ELHT</li>
  <li>As a patient I can use the alter booking feature so that I can rearrange or cancel the appointment of my examination</li>
  <li>As a patient I can learn about the different radiology examinations so that I can be more prepared and less anxious for my appointment</li>
  <li>As a patient I can learn about the necessity and structure of examination requests so that I can complete the online appointment booking more easily</li>
  <li>As a patient I can learn about the different radiology locations in ELHT so that I can make an informed decision about which location will be best for my personal needs and care</li>
  <li>As a patient I can learn the basics of radiation safety so that I can make an informed decision about my care and how the examination may affect me in the future</li>
  <li>As a patient I can learn about how and where I will the results of my examination so that my care can be managed quickly and effectively with minimal delays</li>
  <li>As a patient I can learn about the basic management of the department so that make an informed decision about how my care will be managed when I attend for my examination</li>
  <li>As an external company I can contact the radiology department so that there can be a mutually beneficial relationship between my company and the NHS by having my products tested and used by the radiology department</li>
  <li>As a site administrator I can create, read, edit and delete examination appointments on patient's behalf so that patients who are unable to use the online booking system are still able to book appointments</li>
  <li>As a radiology member of staff I can manage my day-to-day workload by knowing in advance which patients are coming to the department so that I can manage my time and the patient's care more effectively</li>
</ol>

#### Feasibility vs Importance

The features in the table below have been taken from the user stories above. Generic features found in most websites will also be implemented such as nav-bar, footer, obvious website purpose etc.

<table>
    <tr>
        <th>Opportunity/Feature</th>
        <th>Feasibility/Viability (score out of 5)</th>
        <th>Level of Importance (score out of 5)</th>
        <th>In or out?</th>
    </tr>
    <tr>
        <td>Contact Form</td>
        <td>4</td>
        <td>4</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>Instant Messaging Service</td>
        <td>1</td>
        <td>2</td>
        <td>OUT</td>
    </tr>
    <tr>
        <td>X-ray booking form</td>
        <td>3</td>
        <td>5</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>CT booking form</td>
        <td>3</td>
        <td>4</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>MRI booking form</td>
        <td>2</td>
        <td>4</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>Ultrasound booking form</td>
        <td>3</td>
        <td>4</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>Mammogram booking form</td>
        <td>3</td>
        <td>4</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>Other examination booking form</td>
        <td>3</td>
        <td>3</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>Alteration of examination booking for patients</td>
        <td>3</td>
        <td>3</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>Educational section on the different examination types</td>
        <td>5</td>
        <td>3</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>Educational section on radiology requests</td>
        <td>5</td>
        <td>2</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>Educational section on the different radiology locations throughout ELHT</td>
        <td>5</td>
        <td>3</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>Educational section on the basics of radiation safety</td>
        <td>5</td>
        <td>2</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>Educational section on how and where to obtain the examination results</td>
        <td>5</td>
        <td>2</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>Educational section on departmental procedures in radiology</td>
        <td>5</td>
        <td>2</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>Section to encourage external companies to contact radiology</td>
        <td>5</td>
        <td>1</td>
        <td>IN</td>
    </tr>
    <tr>
        <td>Administration page to manage patient bookings</td>
        <td>3</td>
        <td>4</td>
        <td>IN</td>
    </tr>
    <tr>
        <td></td>
        <td>Average Viability x number of features:<br> 63</td>
        <td>Sum of Importance:<br> 52</td>
        <td></td>
    </tr>
</table>

As we can see from the table above, the viability is higher than the importance, which is good because that means most of the features are able to be implemented, however I must be careful not to implement features that would be unnecessary for the web application and result in time that could have been better spent on more important features. I must also be careful to stay within the scope of my own coding limitations - implementing features that I have little experience of could cause a high likelihood of bugs and errors in the web application which would in turn reduce the potential of a positive user experience. The main purpose of the web application is for patients to be able to book appointments - therefore all of the booking features I have put as fairly high importance; however my knowledge and confidence of using the back-end frameworks needed to be able to implement these features is lacking, and as such I have but the viability as fairly low. I am hoping that during the process of developing this project that my confidence in using frameworks such as Django will improve and I will be able to implement the more difficult booking forms with more ease.

The table above has been plotted into a graph (below) to easily visualise the features that will be implemented into the web application and which ones won't be:
<ul>
    <li>The features in the pink section will be implemented</li>
    <li>The features in the grey section could/should be implemented however I might find it difficult due to my own coding knowledge</li>
    <li>The features in the turquoise section will not be implemented as it would be unwise to focus on these features until a later date</li>
</ul>

<img src="readmeassets/featuretable.png" width="450px"><br>
<img src="readmeassets/featuregraph.png" width="600px"> 

### Scope

Due to the pitfalls of developing a website based on the MVP (Minimum Viable Product) model such as lack of user experience and enjoyment due to a lack of content, it is sometimes more beneficial to develop a website based on MMP (Minimum Marketable Product). However due to the more advanced coding that I'll be using in this project and the possible time constraints I might find myself in, I am going to create the website based on MVP. This will allow the basic functions of the website to be implemented and have the website be usable but not necessarily complete with all of the discussed features in place. One of the main advantages of creating an MVP is we can gauge the reaction of users before implementing more features, to ensure that the overall necessity for the web application is there, meaning less time is potentially wasted on a product that isn't going to be used by our target audience.

By using the MVP model we will:
<ul>
    <li>Create a clear website with enough content for the users to establish the usefulness of the web application</li>
    <li>Result in a website with medium levels of UX, but still enough to be user friendly for our target audiences</li>
    <li>Meet the needs of the business and user on the most basic levels</li>
</ul>
While following the MVP model, to meet the user and business goals, our website will include:
<ul>
    <li>A nav-bar on all pages to be able to navigate to separate pages on the website</li>
    <li>Links to associated social media on all pages within the footer</li>
    <li>A contact form for site users to be able to contact the radiology department</li>
    <li>Booking forms for a range of modalities for patients to be able to arrange their own radiology examinations (not necessarily all of them)</li>
    <li>Educational pages for the user to be able to learn more about their examination and the steps around it</li>
    <li>An admin login for site admins to be able to manage patient's bookings</li>
</ul>

### Structure

I have chosen to carry out a linear method of design for this website application as there should be a logical way for the user to view certain things. By having multiple pages we can separate information into logical sections to make it easier for the user to find what they are looking for particularly for the users that may find it more difficult to navigate websites. The navigation bar at the top of all of the pages allows the user to easily navigate to the page of the website they are most interested in. There are also certain pages (such as on the home page) that have their own internal navigation sections - for example on the home page there is a navigation section for the user to be able to navigate to particular booking forms. 

<strong>On ALL PAGES</strong>: There will be a nav bar stretching across the full width of the users device - this will be fully responsive and collapse down to a togggle-able icon at smaller screen sizes. There will also be a 2-part footer consisting of useful links for the site user such as a contact page, contact numbers, the ELHT Trust slogan (in logo form), a staff list, opening times, a complaints link, the privacy policy, admin login and links to social media.<br>

<strong>On home.html</strong>: This will consist of a large full width hero-image with overlying text to give the user an instant idea as to the function of the website. Below the hero image will be the links to the booking pages, there will be separate links for each examination type as each examination needs different questions answered. Below this there will be another section with links to the other two main areas of the website - patient information and examination information. The last section on this page will consist of an invitation to external companies to partner with ELHT radiology, but will also include reassurance to patients that the department has high-end and reliable equipment.<br>

<strong>On information/{info_section}.html</strong>: These pages will consist of information on various subjects such as radiation safety, how the department runs, different locations the patient can go for their images, radiology requests and how to get results after the examination.<br>

<strong>On examinations/{exam_type}.html</strong>: These pages will give a more in depth view for the patient as to what will happen during their radiology examination. It is the hope that this will reduce examination anxiety and encourage the patient to attend their appointment with less nerves.<br>

<strong>On book/{exam_type}.html</strong>: These pages will show the individual booking forms for the specific examination type.<br>

<strong>On contact.html</strong>: This will consist of the main contact form, an interactive google map showing the various locations that the patients can go for their examination. Contact details of the various departments, as well as downloadable site maps of the three biggest hospitals in ELHT.<br>

<strong>On privacy.html</strong>: This will explain to patients and site visitors as to how their personal information will be used/shared.<br>

<strong>On 404.html</strong>: This will consist of a simple page with minimal design and a link to direct the site user back to the home page.<br>


### Skeleton

The wireframes for ELHT-RBS website application were made with Balsamiq, they can be found by viewing the images below. As the trend for mobile browser usage has been on an upwards trend for the last 10 years in Europe culminating in a crossover of hardware usage in the recent year, it could be assumed that these trends will continue and result in users opting more and more for a mobile browser instead of a desktop. Due to this assumed continuing trend I have chosen to take a mobile-first approach to the design process. A Mobile-First Approach refers to the practice of designing and/or developing an online experience for mobile before designing for desktop web or any other device. Taking a Mobile First approach aims to reverse the workflow of designing for desktop and scaling down the design for mobile afterwards. Wireframes were made for mobile and desktop devices to ensure user friendly UX was employed throughout, I also included a tablet wireframe for the home page as this is the page that will be most visited and must look great on all screen sizes otherwise this will risk users navigating away due to un-responsiveness.

#### home.html
<img src="readmeassets/wire1-index.png">

#### On book/{exam_type}.html
<img src="readmeassets/wire2-book.png">

#### On information/requests.html
<img src="readmeassets/wire3-request.png">

#### On information/locations.html
<img src="readmeassets/wire4-locations.png">

#### On information/radiation.html
<img src="readmeassets/wire5-radiation.png">

#### On information/results.html
<img src="readmeassets/wire6-results.png">

#### On information/department.html
<img src="readmeassets/wire7-dept.png">

#### On examinations/{exam_type}.html
<img src="readmeassets/wire8-exam.png">

#### On contact.html
<img src="readmeassets/wire9-contact.png">

The wireframes were created during the website application's initial design process, as such there are changes between the layout of the wireframes and the final layout/design of the finished website. Wireframes were not made for the privacy policy or the 404 page as these will be very basic layouts with very little styling.

### Surface
#### Typography
As recommended in various literature, I have chosen to use sans-serif fonts throughout the website as these are more user friendly. I used Google Fonts to find the typography that I wanted to use for the website.

The fonts I used for the text body of the website was 'Lato' as this font is easy to read which is needed when there is large amounts of information to be read and absorbed by users, it has a modern feel, and is a popular font for many websites. The back-up font is 'Sans-Serif' just in case the font import link fails. The font used for headings is 'Roboto' this is also a very popular font recommended by many websites that cater to the needs of individuals with neurodivesity. As this is a medical related website, I wanted to keep the fonts as user friendly and clean as possible.

#### Colour Scheme
The main colour theme of the website is blues/greys and white. This keeps the website feeling modern and clean and also keeps it feeling fairly medical.

#### Icons
The main icons used throughout the website are the NHS icon and icons related to ELHT, these were taken from the ELHT Website.<br><br>
<img src="readmeassets/logo1.png" height="70px"><br><br>  
<img src="readmeassets/logo2.png" height="100px"><br><br>
<img src="readmeassets/logo3.png" height="100px"><br><br>
<img src="readmeassets/logo4.png" height="100px"><br><br>
<img src="readmeassets/logo5.png" height="100px">

The favicon was handmade by myself using the ELHT theme colours of blue, green purple and pink.<br><br>
<img src="readmeassets/fav.png" height="200px">


#### Images & Videos
All images throughout the site were taken from either Pexels, Pixabay or Shutterstock - royalty free websites. I have tried to make all the images used as relevant to the page they are on as possible, as well as keeping them simple and 'clean'. 

<img src="static/images/hero.jpg" height="300px"> <img src="static/images/extra.jpg" height="300px">
<img src="readmeassets/white2.jpg" height="300px"> <img src="static/images/advert.jpg" height="300px">
<img src="static/images/radiographer.png" height="300px"> <img src="static/images/info-board-hero.jpg" height="300px">
<img src="static/images/exam-board-hero.jpg" height="300px"> <img src="static/images/contact-hero.jpg" height="300px">
<img src="static/images/book-hero.jpg" height="300px"> <img src="static/images/xray-hero.jpg" height="300px">
<img src="static/images/ct-hero.jpg" height="300px"> <img src="static/images/mri-hero.jpg" height="300px">
<img src="static/images/nm-hero.jpg" height="300px"> <img src="static/images/us-hero.jpg" height="300px">
<img src="static/images/dexa-hero.jpg" height="300px"> <img src="static/images/angio-hero.jpg" height="300px">
<img src="static/images/fluoro-hero.jpg" height="300px"> <img src="static/images/mammo-hero.jpg" height="300px">
<img src="static/images/dept-hero.jpg" height="300px"> <img src="static/images/locations-hero.jpg" height="300px">
<img src="static/images/radiation-hero.jpg" height="300px"> <img src="static/images/requests-hero.jpg" height="300px">
<img src="static/images/results-hero.jpg" height="300px"> 

## Technologies
<img src="https://img.shields.io/badge/HTML-5-red">  <img src="https://img.shields.io/badge/CSS-3-blue">  <img src="https://img.shields.io/badge/JavaScript-ES6-yellow">  <img src="https://img.shields.io/badge/Python-3-9cf">  <img src="https://img.shields.io/badge/Django-3-green"><br>
<img src="https://img.shields.io/badge/Bootstrap-5.1-purple">  <img src="https://img.shields.io/badge/Git-2.33.1-red">  <img src="https://img.shields.io/badge/GitPod-.io-orange">  <img src="https://img.shields.io/badge/Balsamic-4.3.3-darkgrey"><br>
<img src="https://img.shields.io/badge/Slack-4.21-pink">  <img src="https://img.shields.io/badge/PostgreSQL-14.0-blue">  <img src="https://img.shields.io/badge/Gunicorn-20.1.0-green"><br>
<img src="https://img.shields.io/badge/Chrome-DevTools-yellow">  <img src="https://img.shields.io/badge/Google-Fonts-green">  <img src="https://img.shields.io/badge/Favicon-.io-green"><br>
<img src="https://img.shields.io/badge/W3C-validation-red">  <img src="https://img.shields.io/badge/JigsawW3C-validation-blue">  <img src="https://img.shields.io/badge/JSHint-Validation-yellow"><br>
<img src="https://img.shields.io/badge/PEP8-online-blue">  <img src="https://img.shields.io/badge/WAVE-WebAccessTool-pink">  <img src="https://img.shields.io/badge/Heroku-Deployment-purple">

## Features

### Deciding what to implement
Using the table from the Strategy Plane of the UX section, I was able to determine what could be implemented and what would be better being left out by using a viability/importance chart. Those features that were plotted in the graph in the pink area were those that were determined to be both important AND viable enough to be implemented.<br>

### Implemented Features
From the table, I was able to recognise which features were more likely to have a positive impact on the website and implement the following:
<ul>
    <li><em>A Contact form for site users to be able to get in contact with site admins/management</em> - I felt this was extremely important to enable site users and patients to be able to contact the department. As the website doesn't have the feature of patients being able to edit/cancel their own bookings, I wanted to have a contact form feature to give patients an easy way to contact us.</li>
    <li><em>Booking forms for all radiology modalities to enable site users to be able to arrange radiology appointments</em> - The main purpose of the website is to enable patients to self-appoint once they have a radiology request, as such I had to implement a feature to allow patients to do this. The radiology department is split into modalities, so I have implemented a separate booking form for each modality, so members of staff in the department can look at their own modality list and manage their workflow for the day.</li>
    <li><em>Educational pages on the different radiology modalities</em> - from experience, I have found that a lot of patients are unaware why they are going for a certain radiology examination and are unaware of the differences between them. By having these information pages, it will enable patients to learn about their examination and enable the patient to give informed consent when they have their procedure/images.</li>
    <li><em>Educational pages on other aspects of the radiology department/booking process</em> - from experience, I have found that many patients are confused about certain aspects of their referral/examination procedure and are nervous when they attend for their examination. By having information pages explaining all aspects of the referral/examination/results process, it can reduce the anxiety that some patients feel when attending hospitals.</li>
    <li><em>Ability for site admins to delete/read/update/create appointments for patients on their behalf</em> - This can be achieved via the Django administration page. I had hoped to implement a log in feature for staff members to do this via the website itself, and have a page showing all booked appointments, however due to time constraints and limits in my own coding/django knowledge, I chose to leave this feature out rather than risk a buggy/unfriendly user experience.</li>
</ul>   

### Features left to implement
<ul>
    <li><em>An instant messaging service for patient to be able to contact the radiology department in real-time</em> - by having this feature it would enable patients to be able to contact the radiology department quickly and to be able to get an instant reply. This could be for situations such as if the patient is going to be late for their appointment, or if they need help with completing the booking form. This feature wasn't implemented because it was outside the scope of my own abilities, I haven't been taught how to do this in the code institute lessons, and I didn't want to struggle doing something that isn't necessarily 'important' when there are other ways to achieve a similar goal - e.g. the contact form.</li>
    <li><em>The ability for patients to self-manage their radiology bookings</em> - I had hoped to implement this feature, and did start to implement it. However, I found myself struggling to do this with my lack of django experience. I also think that due to the 9 different booking forms, it made things more complicated. I started my generating a patient reference number, and I was going to use this in a single input form to generate the rest of the booking information (time, date, location etc.) to then enable the patient to either cancel or edit their booking. After a few failed attempts, I found this was much easier said than done, and took the decision to leave this feature out rather than cause potential errors with the website. If I had more time, I would likely try and find a way to implement this as I feel this is an important feature to add to the usability of the website and the overall satisfaction that users may gain.</li>
</ul>

## Testing
### Functionality
### Compatibility
### User Testing Stories
### Code Validation
### Issues Found During Deployment
### Accessibility
### Performance Testing

## Deployment
A live demo of the website can be found <a href="#" target="_blank">**HERE**</a><br>

### Project Creation
This project was created on GitHub and Edited in GitPod by carrying out the following:
<ol>
    <li>A new repository was created using 'Code-Instutute-Org/gitpod-full-template'</li>
    <li>A meaningful name was given to the new repository and 'Create Repository' was selected</li>
    <li>The repository was then opened on GitHub by clicking the 'Gitpod' button to build the GitPod workspace which would allow me to build and edit the code used to make the <em>PROJECT NAME HERE</em> website/application</li>
    <li>Version control was used throughout the project using the following commands in the terminal using Bash
        <ul>
            <li>git add . <strong>OR</strong> git add "file name" - to stage the changes and get them ready for being committed to the local repo.</li> 
            <li>git commit -m "Description of the update" - to save the change and commit the change to the local repo</li>
            <li>git push - to push all committed changes to the GitHub repo associated with the GitPod workspace</li>
        </ul>
    </li>

### Project Deployment
This project was deployed via Heroku by carrying out the following:
<ol>
    <li>Create the gitpod repo from the template via the gitpod button in github.</li>
    <li>Log in to Heroku and create a new app.</li>
    <li>Add the postgres add-on</li>
    <li>Complete the config vars section</li>
    <li>Link Heroku and GitHub accounts together</li>
    <li>Select the repo (via Heroku) that I wanted to make an app of and give it a name in Heroku.</li>
    <li>Click on deploy.</li>
</ol>

### Local Deployment
There are many ways to deploy the project locally on your own device. The ways I will explain here are: Forking, Cloning, GitHub Desktop and Zip Extraction, the steps in these processes are outlined below:

#### Forking the GitHub repo
If you want to make changes to the repo without affecting it, you can make a copy of it by 'Forking' it. This will make sure that the original repo remains unchanged.
<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the repository <a href="#"><strong>HERE</strong></a></li>
    <li>Select the 'Fork' button in the top right corner of the page (under your account image)</li>
    <li>The repo has now been copied into your own repos and you can work on it in your chosen IDE</li>
    <li>If you have any suggestions to make regards to the code to make the site better, you can put in a pull request</li>
    <li>If you want to create a web-app from the repo please follow the instructions in "Project Deployment"</li>
</ol>

#### Cloning the repo with GitPod
<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the Repository <a href="#"><strong>HERE</strong></a></li>
    <li>Select the 'Code' button above the file list on the right had side</li>
    <li>Ensure HTTPS is selected and click the clipboard on the right of the URL to copy it</li>
    <li>Open a new workspace in GitPod</li>
    <li>In the bash terminal type 'git clone [copy url here from step 4]'</li>
    <li>Press enter - the IDE will clone and download the repo</li>
    <li>You can then type 'python3 -m http.server' to host the website locally - this will not run the python file, only allow you to check how the web-app looks.</li>
    <li>If you want to create a web-app from the repo please follow the instructions in "Project Deployment"</li>
</ol>
  
#### Github Desktop
<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the Repository <a href="#"><strong>HERE</strong></a></li>
    <li>Select the 'Code' button above the file list on the right had side</li>
    <li>Select 'Open with GitHub Desktop'</li>
    <li>If you haven't already installed GitHub desktop application - you will need to follow the relevant steps to do this</li>
    <li>The repo will then be copied locally onto your machine</li>
    <li>If you want to create a web-app from the repo please follow the instructions in "Project Deployment"</li>
</ol>

#### Download and extract the zip directly from GitHub
<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the Repository <a href="#"><strong>HERE</strong></a></li>
    <li>Select the 'Code' button above the file list on the right had side</li>
    <li>Select 'Download Zip'</li>
    <li>Once you have the Zip downloaded, open it with your preferred file decompression software</li>
    <li>You can then drag and drop the files from the folder into your chosen IDE or view/edit them on your local machine</li>
    <li>If you want to create a web-app from the repo please follow the instructions in "Project Deployment"</li>
</ol>
  
## Credits
### Code
All code used in this project was taken from the Code Institute lessons, as well as Django's documentation.

### Content
As I have worked in the radiology field for nearly 7 years, all content in the website has been taken from my own knowledge and experience.

### Images
<ul>
    <li>Index/Home page:</li>
        <ul>
            <li>The hero image for index.html can be found <a href="https://www.istockphoto.com/photo/medical-technology-concept-remote-medicine-electronic-medical-record-gm1300745916-392975316"><strong>HERE</strong></a></li>
            <li>The image of the radiographer in the booking links section on index.html can be found <a href="https://www.pexels.com/photo/photo-of-doctor-holding-x-ray-result-4225880/"><strong>HERE</strong></a></li>
            <li>The background image for the review section on index.html can be found <a href="https://www.istockphoto.com/photo/doctor-sees-virtual-images-of-the-patient-gm928162118-254586367"><strong>HERE</strong></a></li>
            <li>The background image for other links section on index.html can be found <a href="https://www.istockphoto.com/photo/portrait-of-a-beautiful-medical-specialist-working-as-an-orthopedist-gm1312204391-401081571"><strong>HERE</strong></a></li>
            <li>The background image for the collaboration/advertisement section on index.html can be found <a href="https://www.istockphoto.com/photo/modern-operating-room-in-a-hospital-generated-digitally-gm1281627829-379609702"><strong>HERE</strong></a></li>
        </ul>   
    <li>Information Pages:</li>
        <ul>
            <li>The background image for the patient information board can be found <a href="https://www.istockphoto.com/photo/medical-technology-concept-gm1127069581-296928242"><strong>HERE</strong></a></li>
            <li>The background image for the department information page can be found <a href="https://www.istockphoto.com/photo/waiting-area-in-hospital-gm1053085842-281347392"><strong>HERE</strong></a></li>
            <li>The background image for the locations information page can be found <a href="https://www.istockphoto.com/photo/a-white-3d-rendered-image-of-the-united-kingom-gm93293761-9241291"><strong>HERE</strong></a></li>
            <li>The background image for the radiation information page can be found <a href="https://www.istockphoto.com/photo/hospital-ai-gm1057025412-282493246"><strong>HERE</strong></a></li>
            <li>The background image for the request information page can be found <a href="https://www.istockphoto.com/photo/cropped-close-up-shot-of-doctor-giving-prescriptions-medications-to-female-patient-gm1352061644-427596207"><strong>HERE</strong></a></li>
            <li>The background image for the results information page can be found <a href="https://www.istockphoto.com/photo/medical-diagnosis-in-the-digital-age-gm1127376129-297113241"><strong>HERE</strong></a></li>
        </ul>  
    <li>Examination Information Pages:</li>
        <ul>
            <li>The background image for the patient examination information board can be found <a href="https://www.istockphoto.com/photo/healthcare-and-medicine-covid-19-doctor-holding-and-diagnose-virtual-human-lungs-gm1220059276-357092137"><strong>HERE</strong></a></li>
            <li>The background image for the x-ray information page can be found <a href="https://www.istockphoto.com/photo/ct-scan-device-in-modern-hospital-gm1255307625-367203639"><strong>HERE</strong></a></li>
            <li>The background image for the CT information page can be found <a href="https://www.istockphoto.com/photo/medical-ct-or-mri-or-pet-scan-standing-in-the-modern-hospital-laboratory-gm1074166156-287587561"><strong>HERE</strong></a></li>
            <li>The background image for the MRI information page can be found <a href="https://www.istockphoto.com/photo/mri-scan-device-gm906612074-249859283"><strong>HERE</strong></a></li>
            <li>The background image for the Ultrasound information page can be found <a href="https://www.istockphoto.com/photo/doctor-prepare-an-ultrasound-machine-for-the-diagnosis-of-a-patient-doctor-puts-gm1184471397-333441192"><strong>HERE</strong></a></li>
            <li>The background image for the Nuclear Medicine information page can be found <a href="https://www.istockphoto.com/photo/gamma-camera-gm186831409-17106701"><strong>HERE</strong></a></li>
            <li>The background image for the Mammography information page can be found <a href="https://www.istockphoto.com/photo/operating-room-with-mammography-x-ray-system-machine-in-hospital-laboratory-cancer-gm1132664249-300370098"><strong>HERE</strong></a></li>
            <li>The background image for the Dexa information page can be found <a href="https://www.istockphoto.com/photo/medical-scan-gm185093593-19277599"><strong>HERE</strong></a></li>
            <li>The background image for the Angiography Medicine information page can be found <a href="https://www.istockphoto.com/photo/x-ray-monitoring-of-surgical-procedure-in-the-hospital-cathlab-gm1139755594-304750515?utm_source=pixabay&utm_medium=affiliate&utm_campaign=SRP_image_noresults&referrer_url=http%3A%2F%2Fpixabay.com%2Fimages%2Fsearch%2Fangiography%2F&utm_term=angiography"><strong>HERE</strong></a></li>
            <li>The background image for the Fluoroscopy information page can be found <a href="https://www.istockphoto.com/photo/barium-enema-or-be-is-image-of-large-bowel-after-injection-of-barium-contrast-fill-gm1326802025-411372792"><strong>HERE</strong></a></li>
        </ul> 
    <li>Other Pages:</li>
        <ul>
            <li>The background image for the contact page and thank you page can be found <a href="https://www.istockphoto.com/photo/social-network-gm1142791580-306657206"><strong>HERE</strong></a></li>
            <li>The background image for the booking pages can be found <a href="https://www.istockphoto.com/photo/stethoscope-on-book-gm155099359-18178003"><strong>HERE</strong></a></li>
        </ul>     
</ul>

### Acknowledgements
<ul>
    <li>
        To my amazing husband-to-be. Without you, I would have had far more mental-breakdowns. You keep me sane and focused and help me look at things in a logical way.
    </li>
    <li>
        To my mentor Nishant Kumar. Your guidance, support and encouragement have been everything.
    </li>
</ul>

## Screenshots

