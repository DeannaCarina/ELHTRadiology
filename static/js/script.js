
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



function sendMail(contactForm) {
    emailjs.send("service_wsng2tl", "template_elhtrbs", {
        "from_name": contactForm.name.value,
        "form_email": contactForm.email.value,
        "form_subject": contactForm.subject.value,
        "form_message": contactForm.message.value
    })
    .then(
        // If the message is successfully sent 
        function(response) {
            console.log("SUCCESS", response);
            alert('Your email has been sent.');
        },
        // If the message does not send
        function(error) {
            console.log("FAILED", error);
        }
    );

    document.getElementById('fillForm').reset(); // Reset form once the message has been sent
    return false; // This is to prevent the page from refreshing when you submit your form 
}