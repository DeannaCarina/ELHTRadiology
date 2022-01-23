
/*jshint sub:true*/

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.datepicker');
    
  });

// BOOKING FORM VALIDATION

function validateForm() {
    
    let formvalid = true;

    // REQUEST NUMBER
    let reqnum = document.forms["bookingForm"]["request_number"].value;
    if (!/^[0-9]{8}$|^$/.test(reqnum)) {
        formvalid = false;
        alert("Your request number should only contain the characters 0-9 and be 8 numbers long. If you don't know your request number, please leave this blank."); 
    }

    // HOSPITAL NUMBER
    let hospnum = document.forms["bookingForm"]["hospital_number"].value;
    if (!/^ICE[0-9]{6}$|^RXR[0-9]{7}$|^$/i.test(hospnum)) {
        formvalid = false;
        alert("Your hospital number should take the format 'RXR' followed by 7 numbers or 'ICE' followed by 6 numbers."); 
    }

    // FIRST NAME & LAST NAME
    let firstname = document.forms["bookingForm"]["first_name"].value;
    let lastname = document.forms["bookingForm"]["last_name"].value;
    if (!/^[a-z_-]{1,50}$/i.test(firstname) || !/^[a-z_-]{1,50}$/i.test(lastname)) {
        formvalid = false;
        alert("Your name should only contain A-Z, a-z or the '-' character and be a maximum of 50 characters long. If your name contains other characters or symbols, please contact the department directly to book your appointment."); 
    }

    
    // DATE OF BIRTH & DATE OF EXAM
    let dateofbirth = document.forms["bookingForm"]["date_of_birth"].valueAsDate;
    let dateofexam = document.forms["bookingForm"]["date_of_exam"].valueAsDate;
    let today = new Date();
    let parseDOB = Date.parse(dateofbirth);
    let parseToday = Date.parse(today);
    let parseDOE = Date.parse(dateofexam);
    if (parseDOB > parseToday) {
        formvalid = false;
        alert("You cannot have a date of birth in the future.");
    }
    if (parseDOE < parseToday) {
        formvalid = false;
        alert("You cannot have an examination date in the past.");
    }

    // TIME OF EXAM
    let examtime = document.forms["bookingForm"]["time_of_exam"].value;
    let timeSplit = examtime.split(":");
    if (timeSplit[0] < 9 || (timeSplit[0] >= 16 && timeSplit[1] >= 30)) {
        formvalid = false;
        alert("Our opening hours are 9am - 4.30pm. Please select a time within our working hours. If you need an out-of-hours appointment, please contact the department directly.");
    }

    // CONTACT NUMBER 
    let contnum = document.forms["bookingForm"]["contact_number"].value;
    if (!/^0[0-9]{1,20}$/.test(contnum)) {
        formvalid = false;
        alert("Please provide a valid phone number between 5 and 20 numbers long using characters 0-9 (Please do not put spaces in your contact number)."); 
    }

    return formvalid;
  }