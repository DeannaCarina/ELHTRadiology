
function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 10,
        center: {
            lat: 53.809688,
            lng: -2.378590
        }
    });

    var labels = " ";

    var locations = [
        { lat: 53.735646, lng: -2.459702 },//RBH 
        { lat: 53.750631, lng: -2.488290 },//BCW  
        { lat: 53.759688, lng: -2.367447 },//AVH  
        { lat: 53.809980, lng: -2.227929 },//BGH  
        { lat: 53.838745, lng: -2.211099 },//PCH  
        { lat: 53.700961, lng: -2.280902 },//RPC  
        { lat: 53.883678, lng: -2.374315 },//CCH  
    ];

    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    var markerCluster = new MarkerClusterer(map, markers, { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
}


document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(elems, options);
  });

  // Or with jQuery

  $(document).ready(function(){
    $('.datepicker').datepicker();
  });


// BOOKING FORM VALIDATION

function validateForm() {
    
    let formvalid = true
    
    // REQUEST NUMBER
    let reqnum = document.forms["xrayForm"]["request_number"].value;
    if (reqnum.length >= 1 && reqnum.length <= 7 || reqnum.length >= 9) {
        formvalid = false;
        alert("Your request number should be 8 numbers long. If you don't know your request number, please leave this blank."); 
    };
    if (!/^[0-9]+$/.test(reqnum) && (reqnum != '')) {
        formvalid = false;
        alert("Your request number should only contain the characters 0-9 and be in the format 12345678. If you don't know your request number, please leave this blank."); 
    };

    // HOSPITAL NUMBER
    let hospnum = document.forms["xrayForm"]["hospital_number"].value;
    if ((hospnum.length >= 1 && hospnum.length <= 9 || hospnum.length >=11) && (hospnum.startsWith("RXR") || hospnum.startsWith("rxr"))) {
        formvalid = false;
        alert("Your hospital (RXR) number should be in the format: 'RXR1234567'. If you don't know your hospital number, please leave this blank");
        return false;
    };
    if ((hospnum.length >= 1 && hospnum.length <= 8 || hospnum.length >=10) && (hospnum.startsWith("ICE") || hospnum.startsWith("ice"))) {
        formvalid = false;
        alert("Your hospital (ICE) number should be in the format: 'ICE123456'. If you don't know your hospital number, please leave this blank");
        return false;
    };
    if ((hospnum.length >=1 && hospnum.length <=8 || hospnum >= 11) || (hospnum.slice(0,3) != '' && hospnum.slice(0,3) != 'RXR' && hospnum.slice(0,3) != 'rxr' && hospnum.slice(0,3) != 'ICE' && hospnum.slice(0,3) != 'ice')) {
        formvalid = false;
        alert("Your hospital number should start with 'RXR' followed by 7 numbers or 'ICE' followed by 6 numbers. If you don't know your hospital number, please leave this blank");
    };

    // FIRST NAME & LAST NAME
    let firstname = document.forms["xrayForm"]["first_name"].value;
    let lastname = document.forms["xrayForm"]["last_name"].value;
    if (firstname.length >= 50 || lastname.length >= 50) {
        formvalid = false;
        alert("Oh no! Your name is too long for our system, please contact us directly to book your appointment."); 
    };
    if (!/^[a-z_A-Z_-]+$/.test(firstname || !/^[a-z_A-Z_-]+$/.test(lastname))) {
        formvalid = false;
        alert("Your name should only contain A-Z, a-z or the '-' character. If your name contains other characters or symbols, please contact the department directly to book your appointment."); 
    };

    
    // DATE OF BIRTH & DATE OF EXAM
    let dateofbirth = document.forms["xrayForm"]["date_of_birth"].valueAsDate;
    let dateofexam = document.forms["xrayForm"]["date_of_exam"].valueAsDate;
    let today = new Date();
    let parseDOB = Date.parse(dateofbirth);
    let parseToday = Date.parse(today);
    let parseDOE = Date.parse(dateofexam);
    if (parseDOB > parseToday) {
        formvalid = false;
        alert("You cannot have a date of birth in the future.");
    };
    if (parseDOE < parseToday) {
        formvalid = false;
        alert("You cannot have an examination date in the past.");
    };

    // TIME OF EXAM
    let examtime = document.forms["xrayForm"]["time_of_exam"].value;
    let timeSplit = examtime.split(":")
    if (timeSplit[0] < 9 || (timeSplit[0] >= 16 && timeSplit[1] >= 30)) {
        formvalid = false;
        alert("Our opening hours are 9am - 4.30pm. Please select a time within our working hours. If you need an out-of-hours appointment, please contact the department directly.");
    };

    // CONTACT NUMBER 
    let contnum = document.forms["xrayForm"]["contact_number"].value;
    if ((contnum.length <= 5 || contnum.length >= 21) || (!/^[0-9]+$/.test(contnum))) {
        formvalid = false;
        alert("Please provide a valid phone number between 5 and 20 numbers long using characters 0-9."); 
    };

    return formvalid;
  };