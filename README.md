
<a href="https://elht-rbs.herokuapp.com/"><h1>ELHT Radiology Booking Service</h1></a>

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
    <li>
        <a href="#overall-thoughts"><strong>Overall Thoughts</strong></a>
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
All images throughout the site were taken from either Pexels, or Shutterstock - stock photo websites. I have tried to make all the images used as relevant to the page they are on as possible, as well as keeping them simple and 'clean'. Below are all the images used - clicking them will open them in a new widow at a larger size.

<img src="static/images/hero.jpg" height="200px"> <img src="static/images/extra.jpg" height="200px">
<img src="readmeassets/white2.jpg" height="200px"> <img src="static/images/advert.jpg" height="200px">
<img src="static/images/radiographer.png" height="200px"> <img src="static/images/info-board-hero.jpg" height="200px">
<img src="static/images/exam-board-hero.jpg" height="200px"> <img src="static/images/contact-hero.jpg" height="200px">
<img src="static/images/book-hero.jpg" height="200px"> <img src="static/images/xray-hero.jpg" height="200px">
<img src="static/images/ct-hero.jpg" height="200px"> <img src="static/images/mri-hero.jpg" height="200px">
<img src="static/images/nm-hero.jpg" height="200px"> <img src="static/images/us-hero.jpg" height="200px">
<img src="static/images/dexa-hero.jpg" height="200px"> <img src="static/images/angio-hero.jpg" height="200px">
<img src="static/images/fluoro-hero.jpg" height="200px"> <img src="static/images/mammo-hero.jpg" height="200px">
<img src="static/images/dept-hero.jpg" height="200px"> <img src="static/images/locations-hero.jpg" height="200px">
<img src="static/images/radiation-hero.jpg" height="200px"> <img src="static/images/requests-hero.jpg" height="200px">
<img src="static/images/results-hero.jpg" height="200px"> 

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
    <li><em>Ability for site admins to delete/read/update/create appointments for patients on their behalf</em> - This can be achieved via the Django administration page and also via the manage/worklist pages which are accessible via the admin dropdown list once an admin has logged in. When a patient goes through the booking process, the appointment is then sent to 'new bookings' for the radiology team to assess and accept based on the information the patient has given. If the appointment is accepted, it is then added to the radiology worklist so the radiology tam know that the patient is coming in for an examination.</li>
</ul>   

### Features left to implement
<ul>
    <li><em>An instant messaging service for patient to be able to contact the radiology department in real-time</em> - by having this feature it would enable patients to be able to contact the radiology department quickly and to be able to get an instant reply. This could be for situations such as if the patient is going to be late for their appointment, or if they need help with completing the booking form. This feature wasn't implemented because it was outside the scope of my own abilities, I haven't been taught how to do this in the code institute lessons, and I didn't want to struggle doing something that isn't necessarily 'important' when there are other ways to achieve a similar goal - e.g. the contact form.</li>
    <li><em>The ability for patients to self-manage their radiology bookings</em> - I had started the project by wanting to create a way for users to manage and edit their own radiology bookings, however from experience of working within a radiology department, it makes more sense for the radiology team to have this ability to ensure the smooth running of the department. If patients need to cancel or rearrange their bookings at the moment within the department, they must contact the department in order for a more suitable appointment to be given to the patient and their original appointment to be passed to another patient who may need it. I have implemented the ability for staff members to view/accept/delete appointments made by patients - this (I find) would be more beneficial to the department and keep staff members aware of their day-to-day work load.</li>
    <img src="readmeassets/spam-email1.png" width="300px">
    <img src="readmeassets/spam-email2.png" width="300px">
</ul>

## Testing
### Functionality
The first phase of my testing regime for the website was to look at the functionality of the website and make sure that it meets the needs of the user on the most basic levels and also to ensure that all the interactive aspects of the website all worked with no problems.
<ul>
    <li>All internal links on the website need to be usable, and open in the same window.
        <ul>
           <li>All nav-bar links are generated through the website by extending from the base.html page. By using jinja templating, this minimises the risk of code errors between pages when certain sections are meant to be perfect replicas of each other. On my first portfolio project for the Code Institute course, one of the errors that I (unfortunately) found after submission was that I hadn't copied over the nav-bar accurately to all of the pages of the site, and as such there were layout errors on one of the pages. By using templating, when checking the links in the navbar work, I only need to check on one of the pages of the website, as I know for certain that all of the nav-bars/headers/footers are exactly the same. The following nav-bar links were all checked and found to be working properly before submission: 
                <ul>
                    <li>There is a hidden link on all pages that is for accessibility purposes and users that use their keyboards for navigation, it is within the header section, and has the purpose of allowing the user to skip past the navigation bar. When the user navigates to a new page, they can press the 'tab' button on their keyboard and then press enter to 'skip navigation'. It saves the user time and means that for each page they navigate to, they don't need to tab through the navigation bar to access other sections of the website.</li>
                    <li>The ELHT Radiology Booking service Logo takes the user to the home page, without opening a new window.</li>
                    <li>The 'Home' link in the nav-bar takes the user to the home page, without opening a new window.</li>
                    <li>Within the 'Patient Information' dropdown of the nav-bar, the 'requests' link takes the user to the request information page of the website without opening a new window.</li>
                    <li>Within the 'Patient Information' dropdown of the nav-bar, the 'locations' link takes the user to the locations information page of the website without opening a new window.</li>
                    <li>Within the 'Patient Information' dropdown of the nav-bar, the 'radiation' link takes the user to the radiation information page of the website without opening a new window.</li>
                    <li>Within the 'Patient Information' dropdown of the nav-bar, the 'results' link takes the user to the results information page of the website without opening a new window.</li>
                    <li>Within the 'Patient Information' dropdown of the nav-bar, the 'department' link takes the user to the department information page of the website without opening a new window.</li>
                    <li>Within the 'Examinations' dropdown of the nav-bar, the 'x-ray' link takes the user to the x-ray examination information page of the website without opening a new window.</li>
                    <li>Within the 'Examinations' dropdown of the nav-bar, the 'CT' link takes the user to the CT examination information page of the website without opening a new window.</li>
                    <li>Within the 'Examinations' dropdown of the nav-bar, the 'MRI' link takes the user to the MRI examination information page of the website without opening a new window.</li>
                    <li>Within the 'Examinations' dropdown of the nav-bar, the 'Ultrasound' link takes the user to the Ultrasound examination information page of the website without opening a new window.</li>
                    <li>Within the 'Examinations' dropdown of the nav-bar, the 'Mammograms' link takes the user to the Mammogram examination information page of the website without opening a new window.</li>
                    <li>Within the 'Examinations' dropdown of the nav-bar, the 'Nuclear Medicine' link takes the user to the Nuclear Medicine examination information page of the website without opening a new window.</li>
                    <li>Within the 'Examinations' dropdown of the nav-bar, the 'Fluoroscopy' link takes the user to the fluoroscopy examination information page of the website without opening a new window.</li>
                    <li>Within the 'Examinations' dropdown of the nav-bar, the 'Angiography' link takes the user to the angiography examination information page of the website without opening a new window.</li>
                    <li>Within the 'Examinations' dropdown of the nav-bar, the 'Dexa' link takes the user to the dexa examination information page of the website without opening a new window.</li>
                </ul>
           </li>
           <li>The links found within the footer were also imported to all pages of the website using Jinga templating, and (much the same as the testing for the nav-bar) I only needed to test the links of the footer in one page to know that they would work everywhere.
                <ul>
                    <li>The 'Privacy' link within the footer takes the user to the privacy policy page without opening in a new window.</li>
                    <li>The 'Contact' link within the footer takes the user to the contact page without opening a new window.</li>
                </ul>
           </li>
           <li>The links found on index.html that link the user to other pages were checked before submission:
                <ul>
                    <li>Within the hero section of index.html, there is a link 'Book an appointment' that the user can see as soon as the user navigates to the website, this takes the user to the next section of the same page and shows the user links to specific booking forms.</li>
                    <li>In the section that links the user to specific booking pages, there are 9 links (one for each radiology modality) that take the user to the modality they wish to book an appointment for. These were all checked before submission and navigate the user to the booking pages without opening in a new window.</li>
                    <li>In the section titled 'Looking for information about your visit to radiology?' there are two internal links, one that navigates to the information board, and the other to the examination board. These pages basically do the same job as the nav-bar dropdown lists and the likelihood is they won't be used very often, however I wanted these to be an option for the user incase they use the 'skip navigation' option when using keyboard navigation.</li>
                    <li>In the last section of the index page, there is an internal link to take the user to the contact page, this was checked before submission and takes the user to the contact page without opening in a new window.</li>
                </ul>
           </li>
           <li>On all of the examination information pages there is an internal link to take the user to the specific modality booking page. From a UX perspective, I found this made sense as when patient navigates to the website, they may see the 'examinations' link in the nav-bar and assume this is the quickest way to book an appointment, so I wanted to make sure there is a way to get to the booking pages in multiple ways. I also felt it was important for users to have a way to learn and understand their appointment before booking so they have informed consent around their examination and know in advance wat they will be having done.
                <ul>
                    <li>The internal link on the 'xray' information page takes the user to the xray booking form page.</li>
                    <li>The internal link on the 'CT' information page takes the user to the CT booking form page.</li>
                    <li>The internal link on the 'MRI' information page takes the user to the MRI booking form page.</li>
                    <li>The internal link on the 'Ultrasound' information page takes the user to the Ultrasound booking form page.</li>
                    <li>The internal link on the 'Mammograms' information page takes the user to the Mammogram booking form page.</li>
                    <li>The internal link on the 'Nuclear Medicine' information page takes the user to the Nuclear Medicine booking form page.</li>
                    <li>The internal link on the 'Fluoroscopy' information page takes the user to the Fluoroscopy booking form page.</li>
                    <li>The internal link on the 'Angiography' information page takes the user to the Angiography booking form page.</li>
                    <li>The internal link on the 'Dexa' information page takes the user to the Dexa booking form page.</li>
                </ul>
           </li>
           <li>There are some other internal links dotted throughout the website that were all checked before submission:
                <ul>
                    <li>On the nuclear medicine information page there is an internal link to the CT information page, as some Nuclear Medicine scans use CT technology as part of the examination. This link was checked and takes the user to the CT page without opening in a new window.</li>
                </ul>
           </li>
        </ul>    
    </li>       
    <li>All external links on the website need to be usable, and open in a new window.
        <ul>
            <li>The links within the footer of all pages were imported using jinja templating, and much the same as the header and nav-bar, I only need to check these on one page to know that they work.</li>
                <ul>
                    <li>The external link to facebook in the footer, takes the user to the main facebook page by opening it up in a new tab.</li>
                    <li>The external link to twitter in the footer, takes the user to the main facebook page by opening it up in a new tab.</li>
                </ul>
            </li>
            <li>The other external links on the website that were all checked before submission:</li>
                <ul>
                    <li>The download link in the contact page to show the map for RBH will download the file and open it in a new tab.</li>
                    <li>The download link in the contact page to show the map for BGH will download the file and open it in a new tab.</li>
                    <li>The link found in the radiation information page in the 'Can I wear a lead gown' section navigates the user to the 'StatNews' website in a new tab.</li>
                    <li>The link found in the warning banner at the top of the page for 'educational purposes' will link the user to my GitHub profile, I'm hoping this will lessen the amount of emails I get from companies trying to sell me their products. The warning banner also has a 'close' button that will remove the banner if the user choses not to see it.</li>
                </ul>
            </li>
        </ul>    
    </li>  
    <li>All elements with an associated psuedo class work when the action is carried out (e.g. Hover).
        <ul>
            <li>All buttons will change colour when the user hovers over them. These include the 'book an appointment' button in index.html, the booking form links in index.html, the extra buttons in index.html that navigate to the examination and information boards, the button in the last section that navigates to the contact page, the buttons used in all forms to send the form (for either booking or contact), the buttons for downloading the maps in contact.html, and the buttons in the examination and information boards that take the user to the relevant pages.
                <ul>
                    <li><img src="readmeassets/gif-indexbook.gif"></li>
                    <li><img src="readmeassets/gif-bookinglinks.gif"></li>
                    <li><img src="readmeassets/gif-links.gif"></li>
                    <li><img src="readmeassets/gif-contactlink.gif"></li>
                    <li><img src="readmeassets/gif-contactbutton.gif"></li>
                    <li><img src="readmeassets/gif-bookbutton.gif"></li>
                    <li><img src="readmeassets/gif-examboard.gif"></li>
                    <li><img src="readmeassets/gif-infoboard.gif"></li>
                    <li><img src="readmeassets/gif-download.gif"></li>
                </ul>
            </li>
            <li>Other elements with associated psuedo classes will work when a certain action is carried out (e.g. hover or focus)
                <ul>
                    <li>All form inputs will change background colour when hovered and form inputs will stay the hovered colour when the user clicks in the input field.<br>
                        <img src="readmeassets/gif-contactform.gif"><br>
                        <img src="readmeassets/gif-bookform.gif">
                    </li>
                    <li>All examination information boxes will go fully opaque when the user hovers over them to lessen any potential background distraction.<br>
                        <img src="readmeassets/gif-examinfo.gif">
                    </li>
                    <li>
                        The 'hidden' skip navigation link will come into view if the first thing the user presses on going to the website is the 'tab' button on their keyboard.<br>
                        <img src="readmeassets/gif-skipnav.gif">
                    </li>
                </ul>
            </li>
        </ul>  
        <ul>
            <li>All links will have subtle style changes when the user hovers over them. This includes all nav-bar links including those in the dropdown lists, the links in the footer, and any other links throughout the website.
                <ul>
                    <li><img src="readmeassets/gif-nav.gif"></li>
                    <li><img src="readmeassets/gif-footer.gif"></li>
                    <li><img src="readmeassets/gif-warning.gif"></li>
                </ul>
            </li>
        </ul>
    </li>
    <li>
        All forms within the website give the user instant feedback to reassure them that the form has worked. All forms give a notification email to the user/patient as well as site admin to give real-time feedback/notifications. All form submissions update the Django Postgres Database.
        <ul>
            <li>The image below shows the emails received in the account I used as a 'patient' to book radiology appointments, and the email account I used as the 'admin'. These show the notification emails from both a patient and admin perspective when a new booking is made. All of the emails went through with no problems.<br>
            <img src="readmeassets/check-emails.png"></li>
            <li>The image below shows the updated Django database for each radiology modality when a new booking is made. All bookings went through with no problems, a new patient booking reference number was generated each time and all patient submitted data was transferred.<br>
            <img src="readmeassets/check-forms.png"></li>
        </ul>
    </li>     
</ul><br>

I tested the usability and intuitiveness of the website using different focus groups divided by age: <br>
<table>
    <tr>
        <th>Age Group</th>
        <th>Quantity</th>
        <th>Comments</th>
    </tr>
    <tr>
        <td><strong>16-25</strong></td>
        <td>3</td>
        <td>
            <ul>
                <li>All users knew the purpose of the website on first navigation.</li>
                <li>All users found the website easy to navigate and knew where to go for information and to book an appointment.</li>
                <li>All users found the website well-styled and pleasant to look at.</li>
                <li>All users used their phones.</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong>26-35</strong></td>
        <td>11</td>
        <td>
            <ul>
                <li>All users knew the purpose of the website on first navigation.</li>
                <li>All users found the website easy to navigate and knew where to go for information and to book an appointment.</li>
                <li>All users found the website well-styled and pleasant to look at.</li>
                <li>8 users used their phones, 3 used their laptops.</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong>36-45</strong></td>
        <td>6</td>
        <td>
            <ul>
                <li>All users knew the purpose of the website on first navigation.</li>
                <li>All users found the website easy to navigate and knew where to go for information and to book an appointment.</li>
                <li>All users found the website well-styled and pleasant to look at.</li>
                <li>2 user used their computers, 1 used their MacBook, 3 used their phones.</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong>46-55</strong></td>
        <td>3</td>
        <td>
            <ul>
                <li>All users knew the purpose of the website on first navigation.</li>
                <li>All users found the website easy to navigate and knew where to go for information and to book an appointment.</li>
                <li>All users found the website well-styled and pleasant to look at.</li>
                <li>All users used their phones.</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong>56+</strong></td>
        <td>7</td>
        <td>
            <ul>
                <li>All users knew the purpose of the website on first navigation.</li>
                <li>All users found the website easy to navigate and knew where to go for information and to book an appointment.</li>
                <li>All users found the website well-styled and pleasant to look at.</li>
                <li>2 users used their iPads, 1 used their laptop and 4 used their phones.</li>
            </ul>
        </td>
    </tr>
</table><br>

### Compatibility

The second phase of my testing regime for the website was to ensure that the website is compatible through a range of devices, screen sizes and internet browsers. Throughout the development process, the website was tested on a number of devices: A 17.3 inch windows laptop, a 15.3 inch windows laptop, a 16 inch MacBook Pro, an 8 inch Samsung Galaxy Tab A, a 10.2 inch iPad, A Samsung Galaxy S20 Ultra and A Huawei P30 Pro. It was also tested in Chrome, Firefox, Internet Explorer and Safari as well as Samsung's own internet browser. By also using Chrome Dev Tools, I was able to manually change the screen size to see when elements within the web pages 'break', by using this method, I could pinpoint the exact screen widths and heights to be defined in the CSS media screen queries and alter the stylings to fit accordingly. The videos below shows how I checked the responsiveness of the website at all screensizes.

<img src="readmeassets/gif-responsive.gif"><br>
<img src="readmeassets/gif-responsive2.gif"><br>
<img src="readmeassets/gif-responsive3.gif"><br>
<img src="readmeassets/gif-responsive4.gif"><br>
<img src="readmeassets/gif-responsive5.gif"><br>
<img src="readmeassets/gif-responsive6.gif"><br>

### User Testing Stories
The third phase of my testing regime was to ensure that all user stories identified in the Strategy plane have been acknowledged and achieved.<br><br>

<em>"As a Patient I can contact the radiology department so that I can discuss my radiology appointments/examinations" & "As an external company I can contact the radiology department so that there can be a mutually beneficial relationship between my company and the NHS by having my products tested and used by the radiology department"</em><br>
<img src="readmeassets/user-contact.png"><br>

>On the front-end, the contact form is designed and styled using Bootstrap with some small changes to this via the CSS. On the back-end the form functionality comes from Django's built-in send_mail feature. The user can access this form via the button on the home page where there is a call to action for external companies to contact the department, or via the footer on all pages. When on the contact page, there is some small psuedo-classes for the form which happen when the user hovers over the form inputs and when the user clicks on an input, this is to help users know which input they are currently on, as well as take glare off the white background of the form input for those with sensory difficulties such as autism. When the user submits the form, they will be directed to a 'thank you' page to reassure the user that the message has gone through. The user will also receive a confirmation email if they have put in a valid email address. A notification email will also be sent to the email account I set up for the ELHT RBS project (elhtrbs@gmail.com) so site admins get a real-time notification of when a user has used the contact form.<br><br>

<em>"As a patient I can use the examination booking form so that I can book an appointment at radiology ELHT"</em><br>
<img src="readmeassets/user-book.png"><br>

>On the front-end all of the booking forms were designed and styled using Bootstrap with some small changes to this via the CSS. I chose to create these forms the the HTML pages rather than through the forms.py file and generate them via Django. I chose to do this for a number of reasons: To make it easier for styling, to be able to add the information hover feature to give a more in-depth explanation of each form field, to do specific form-validation via JavaScript. There may have been ways to do this with with a forms.py, however my minimal knowledge of python and django meant that I wasn't very comfortable implementing this, and chose to stick with what I know to minimise potential bugs. When the user has completed the form, they will get a message generated via Django messages at the top of the form confirming their name, the exam time, date and location. The user will also receive an email with this information, and a notification will be sent to ELHT RBS email to alert site admins that there has been a new booking in real-time. To make it easier for site admins to find a specific booking, users will also be given a Booking reference number which is generated using the pattern [first two letters of the exam type][patient surname][time and date of exam in Epoch format]. All information the user inputs into the form (as well as the generated reference number) will be sent to the Django admin panel which can be seen, edited and deleted by site administrators. Site admins can also create appointments in the Django admin panel if a user is unable to do this in the main website.<br><br>

<em>"As a patient I can learn about the different radiology examinations so that I can be more prepared and less anxious for my appointment"</em><br>
<img src="readmeassets/user-exams.png"><br>

>There are 9 separate examination information pages - one for each modality, that each contain 4 different information boxes: "Why do you need this examination?", "Is it safe?", "What do you need to do during the examination?" and "What will the practitioner do during the examination?". From the nearly 7 years I have worked in radiology, these questions are the ones that keep coming up time and again. By having these questions pre-answered on the website, I hope that it would make users and potential patients less anxious when they attend the radiology department for their examinations.<br><br>

<em>"As a patient I can learn about the necessity and structure of examination requests so that I can complete the online appointment booking more easily" & "As a patient I can learn about the different radiology locations in ELHT so that I can make an informed decision about which location will be best for my personal needs and care" & "As a patient I can learn the basics of radiation safety so that I can make an informed decision about my care and how the examination may affect me in the future" & "As a patient I can learn about how and where I will the results of my examination so that my care can be managed quickly and effectively with minimal delays" & "As a patient I can learn about the basic management of the department so that make an informed decision about how my care will be managed when I attend for my examination"</em><br>
<img src="readmeassets/user-requests.png"><br>
<img src="readmeassets/user-radiation.png"><br>
<img src="readmeassets/user-results.png"><br>
<img src="readmeassets/user-dept.png"><br>
<img src="readmeassets/user-locations.png"><br>

>There are 5 separate pages which give the user/patient more information on the topics that are most likely to be asked/talked about: Radiology requests, radiation safety, examination results, the department and different locations around ELHT. I have included these in the website for the same reason as I included the examination information pages - to educate and inform users/patients about their examination and to make an informed decision about whether they want to have the examination or not.<br><br>

<em>"As a site administrator I can create, read, edit and delete examination appointments on patient's behalf so that patients who are unable to use the online booking system are still able to book appointments" & "As a radiology member of staff I can manage my day-to-day workload by knowing in advance which patients are coming to the department so that I can manage my time and the patient's care more effectively"</em><br>
<img src="readmeassets/user-admin.png"><br>

>When a site user/patient uses any of the booking forms, all the information the user submits is added to the Django admin panel in sections divided by radiology modality - xray, ct, mri, ultrasound, nuclear medicine, angio, fluoro, dexa & mammo. Site admins can confirm bookings, delete bookings, see bookings that have been requested by patients/users, edit bookings and add bookings. By separating the bookings into modality sections, different departments within radiology will know what bookings they have for a particular day and plan their workload/day accordingly.<br><br>


### Code Validation

Below are screenshots of all the code validation results from all pages within the website. Clicking on an image will open it in a new page as a larger image.
For all HTML, CSS and JavaScript code, these all passed through validation with no errors.

#### CSS
For validating the CSS code within the ELHT RBS project, I used the <a href="https://jigsaw.w3.org/css-validator/">Jigsaw</a> online validator. The CSS came back with no errors.

<img src="readmeassets/val-css.png" width="200px"> 

#### HTML
For validating the HTML code within the ELHT RBS project, I used the <a href="https://validator.w3.org/">W3C Markup</a> online validator. Each page of the website was rin through the validator individually, totalling 28 separate validation reports. All HTML reports came back with no errors.

<img src="readmeassets/val-index.png" width="200px">
<img src="readmeassets/val-contact.png" width="200px"> <img src="readmeassets/val-privacy.png" width="200px"> <img src="readmeassets/val-exam.png" width="200px">
<img src="readmeassets/val-info.png" width="200px"> <img src="readmeassets/val-infoxray.png" width="200px"> <img src="readmeassets/val-infoct.png" width="200px">
<img src="readmeassets/val-infomri.png" width="200px"> <img src="readmeassets/val-infous.png" width="200px"> <img src="readmeassets/val-infomammo.png" width="200px">
<img src="readmeassets/val-infonm.png" width="200px"> <img src="readmeassets/val-infodexa.png" width="200px"> <img src="readmeassets/val-infoangio.png" width="200px">
<img src="readmeassets/val-infofluoro.png" width="200px"> <img src="readmeassets/val-infodept.png" width="200px"> <img src="readmeassets/val-inforadiation.png" width="200px">
<img src="readmeassets/val-inforequests.png" width="200px"> <img src="readmeassets/val-infolocations.png" width="200px"> <img src="readmeassets/val-inforesults.png" width="200px">
<img src="readmeassets/val-bookxray.png" width="200px"> <img src="readmeassets/val-bookct.png" width="200px"> <img src="readmeassets/val-bookmri.png" width="200px">
<img src="readmeassets/val-bookus.png" width="200px"> <img src="readmeassets/val-bookmammo.png" width="200px"> <img src="readmeassets/val-booknm.png" width="200px">
<img src="readmeassets/val-bookdexa.png" width="200px"> <img src="readmeassets/val-bookangio.png" width="200px"> <img src="readmeassets/val-bookfluoro.png" width="200px">


#### JavaScript
For validating the JavaScript code within the ELHT RBS project, I used the <a href="https://jshint.com/">JSHint</a> online validator. I copied the code from the JavaScript file in the assets folder, and also copied the JavaScript code that I had embedded in the base.html and locations.html pages to check they had no errors. All JavaScript within the project came back with no errors.

<img src="readmeassets/val-js1.png" width="300px">
<img src="readmeassets/val-js2.png" width="300px">
<img src="readmeassets/val-js3.png" width="300px">


#### Python
For validating the python code within the ELHT RBS project, I used an online Python PEP8 Linter <a href="http://pep8online.com/">PEP8 ONLINE</a>. I tested all python files that contain content (manage.py, settings.py, urls.py[in the booking dir], urls.py[in ELHT_radiology dir], wsgi.py, asgi.py, models.py, views.py, apps.py and admin.py). The majority of the python files passed without any errors, however there were three files that had line length errors. As these particular errors don't cause any problems with the function of the website or storage of data in the database, I chose to leave these errors rather than risk having problems with the website.

<img src="readmeassets/val-py-manage.png" width="300px">
<img src="readmeassets/val-py-models.png" width="300px">
<img src="readmeassets/val-py-admin.png" width="300px">
<img src="readmeassets/val-py-apps.png" width="300px">
<img src="readmeassets/val-py-urls2.png" width="300px">
<img src="readmeassets/val-py-asgi.png" width="300px">
<img src="readmeassets/val-py-wsgi.png" width="300px">

<img src="readmeassets/val-py-urls.png" width="300px">
<img src="readmeassets/val-py-views.png" width="300px">
<img src="readmeassets/val-py-settings.png" width="300px">


### Issues Found During Deployment
Thankfully, I found no issues during deployment. From the beginning, the project worked really well whether in development mode or in the deployed version. Each time I needed to update a model, things became a bit more complicated - the easiest way I found to overcome these problems was to delete the Heroku Postgres database, and create a new one, then to make migrations, migrate and create a new super user via the Heroku bash console.

### Accessibility
<em>By making websites accessible, we are ensuring that all of our potential users, including people with disabilities, have a decent user experience and are able to easily access information.  By implementing accessibility best practices, I am also improving the usability of the site for all users.</em>

Due to the importance and necessity of accessibility on websites, I have chosen to run all the web pages associated with the ELHT radiology booking service through the <a href="https://wave.webaim.org/" target="_blank">Wave Accessibility</a> tool. I found from carrying out accessibility checks on my previous projects that the Wave Accessibility tool is a very good all-round checker that looks at a range of aspects on a web page and shows which aspects need fixing or altering in line with accessibility best practices. The steps I took from first check to last check are as follows:
<ol>
    <li>Run each page through the <a href="https://wave.webaim.org/" target="_blank">Wave Accessibility</a> tool</li>
    <li>Rectify any errors that resulted from the <a href="https://wave.webaim.org/" target="_blank">Wave Accessibility</a> check regarding code errors and contrast errors</li>
    <li>Re-run the web page through the <a href="https://wave.webaim.org/" target="_blank">Wave Accessibility</a> tool</li>
</ol>

#### Home page, contact page, privacy page, thanks page, 500, 403 and 404
<img src="readmeassets/access-main.png">

#### /information and its sub-pages (Locations, Department, Radiation, Requests and Results)
<img src="readmeassets/access-information.png">

#### /examinations and its sub-pages (xray, computed_tomography, magnetic_resonance, ultrasound, nuclear_medicine, mammography, angiography, fluoroscopy and dexa)
<img src="readmeassets/access-examination.png">

#### /book sub-pages (xray, ct, mri, ultrasound, nm, mammo, angio, fluoro and dexa)
<img src="readmeassets/access-booking.png">

None of the pages had any true errors, however all pages had the same three contrast errors - one in the header and two in the footer. These are on all pages due to the header and footer being placed on all pages via the base template. I have chosen not to address these contrast errors as they are not important to the overall user experience, and changing them would alter the overall look of the logo and make them not be true to the real thing.

### Performance Testing
Below is the report generated from lighthouse via Chrome DevTools for the desktop website, I am really happy that the accessibility score is so high, especially as the website provides a healthcare-related service, however would have liked a higher score on performance (even though the score on this still isn't bad).<br>
<img src="readmeassets/performance.png"><br>

### Django Testing
By following a Django testing tutorial on Youtube, which can be found <a href="https://www.youtube.com/watch?v=IKnp2ckuhzg&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=4"><strong>HERE</strong></a> I have written some basic tests to check the urls.py and the views.py files. I wasn't very confident in doing this, and much prefer carrying out manual testing which can be seen above.

## Deployment
A live demo of the website can be found <a href="https://elht-rbs.herokuapp.com/" target="_blank">**HERE**</a><br>

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
    <li>Add the heroku-postgres add-on</li>
    <li>Complete the config vars section</li>
    <li>Link Heroku and GitHub accounts together</li>
    <li>Select the repo (via Heroku) that you want to make an app of and give it a name in Heroku.</li>
    <li>Click on deploy.</li>
</ol>

### Local Deployment
There are many ways to deploy the project locally on your own device. The ways I will explain here are: Forking, Cloning, GitHub Desktop and Zip Extraction, the steps in these processes are outlined below:

#### Forking the GitHub repo
If you want to make changes to the repo without affecting it, you can make a copy of it by 'Forking' it. This will make sure that the original repo remains unchanged.
<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the repository <a href="https://github.com/DeannaCarina/ELHTRadiology"><strong>HERE</strong></a></li>
    <li>Select the 'Fork' button in the top right corner of the page (under your account image)</li>
    <li>The repo has now been copied into your own repos and you can work on it in your chosen IDE</li>
    <li>If you have any suggestions to make regards to the code to make the site better, you can put in a pull request</li>
    <li>In the console, run: pip install -r requirements.txt</li>
    <li>If you want to create a web-app from the repo please follow the instructions in "Project Deployment"</li>
</ol>

#### Cloning the repo with GitPod
<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the Repository <a href="https://github.com/DeannaCarina/ELHTRadiology"><strong>HERE</strong></a></li>
    <li>Select the 'Code' button above the file list on the right had side</li>
    <li>Ensure HTTPS is selected and click the clipboard on the right of the URL to copy it</li>
    <li>Open a new workspace in GitPod</li>
    <li>In the bash terminal type 'git clone [repo url]'</li>
    <li>Press enter - the IDE will clone and download the repo</li>
    <li>In the console, run: pip install -r requirements.txt</li>
    <li>If you want to create a web-app from the repo please follow the instructions in "Project Deployment"</li>
</ol>
  
#### Github Desktop
<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the Repository <a href="https://github.com/DeannaCarina/ELHTRadiology"><strong>HERE</strong></a></li>
    <li>Select the 'Code' button above the file list on the right had side</li>
    <li>Select 'Open with GitHub Desktop'</li>
    <li>If you haven't already installed GitHub desktop application - you will need to follow the relevant steps to do this</li>
    <li>The repo will then be copied locally onto your machine</li>
    <li>In the console, run: pip install -r requirements.txt</li>
    <li>If you want to create a web-app from the repo please follow the instructions in "Project Deployment"</li>
</ol>

#### Download and extract the zip directly from GitHub
<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the Repository <a href="https://github.com/DeannaCarina/ELHTRadiology"><strong>HERE</strong></a></li>
    <li>Select the 'Code' button above the file list on the right had side</li>
    <li>Select 'Download Zip'</li>
    <li>Once you have the Zip downloaded, open it with your preferred file decompression software</li>
    <li>You can then drag and drop the files from the folder into your chosen IDE or view/edit them on your local machine</li>
    <li>In the console, run: pip install -r requirements.txt</li>
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
<img src="readmeassets/screen1.png">
<img src="readmeassets/screen2.png">
<img src="readmeassets/screen3.png">
<img src="readmeassets/screen4.png">
<img src="readmeassets/screen5.png">

