<?php
/*
Plugin Name: My Custom Plugin
Description: A plugin to fetch XML data from a URL.
Version: 1.0
Author: Your Name
*/


function fetch_xml_data() {
    $url = 'https://autoplius.lt/export/1253580?p=1253580'; // Replace with your actual XML URL
    
    // Fetch XML data from URL
    $response = wp_remote_get($url);
    
    if (is_wp_error($response)) {
        return; // Handle error appropriately
    }

    $body = wp_remote_retrieve_body($response);
    $xml_data = simplexml_load_string($body);

    if ($xml_data === false) {
        return; // Handle error appropriately
    }

    // Process XML data as needed
    foreach ($xml_data->item as $item) {
        // Example: print item titles
        echo esc_html($item->title) . '<br>';
    }
}

// Hook the function to an action (e.g., init)
add_action('init', 'fetch_xml_data');
