
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


// X-RAY FORM VALIDATION

function xrayValidateForm() {
    
    let xrayformvalid = true
    // REQUEST NUMBER
    
    let xrayreqnum = document.forms["xrayForm"]["request_number"].value;
    if (xrayreqnum.length >= 1 && xrayreqnum.length <= 7 || xrayreqnum.length >= 9) {
        xrayformvalid = false;
        alert("Your request number should be 8 numbers long. If you don't know your request number, please leave this blank."); 
    };

    if (!/^[0-9]+$/.test(xrayreqnum) && (xrayreqnum != '')) {
        xrayformvalid = false;
        alert("Your request number should only contain the characters 0-9 and be in the format 12345678. If you don't know your request number, please leave this blank."); 
    };


    // HOSPITAL NUMBER
    let xrayhospnum = document.forms["xrayForm"]["hospital_number"].value;

    if ((xrayhospnum.length >= 1 && xrayhospnum.length <= 9 || xrayhospnum.length >=11) && (xrayhospnum.startsWith("RXR") || xrayhospnum.startsWith("rxr"))) {
        xrayformvalid = false;
        alert("Your hospital (RXR) number should be in the format: 'RXR1234567'. If you don't know your hospital number, please leave this blank");
        return false
    }

    if ((xrayhospnum.length >= 1 && xrayhospnum.length <= 8 || xrayhospnum.length >=10) && (xrayhospnum.startsWith("ICE") || xrayhospnum.startsWith("ice"))) {
        xrayformvalid = false;
        alert("Your hospital (ICE) number should be in the format: 'ICE123456'. If you don't know your hospital number, please leave this blank");
        return false
    }

    if ((xrayhospnum.length >=1 && xrayhospnum.length <=8 || xrayhospnum >= 11) || (xrayhospnum.slice(0,3) != '' && xrayhospnum.slice(0,3) != 'RXR' && xrayhospnum.slice(0,3) != 'rxr' && xrayhospnum.slice(0,3) != 'ICE' && xrayhospnum.slice(0,3) != 'ice')){
        xrayformvalid = false;
        alert("Your hospital number should start with 'RXR' followed by 7 numbers or 'ICE' followed by 6 numbers. If you don't know your hospital number, please leave this blank");
    }
    


    return xrayformvalid
    
  } 