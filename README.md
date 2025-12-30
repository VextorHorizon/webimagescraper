<h1>Web Image Scraper (MVP)</h1> <br>
A lightweight, CLI-based utility built with Python to automate the extraction and downloading of images from any given web page. Designed for speed, utility, and minimalist efficiency. <br>
<h2>Features</h2>
<ul>
<li>CLI-Driven: Fully controlled via command-line arguments using argparse.</li><br>
<li>Auto-Categorization: Automatically sorts and filters images into PNG, JPG, and WEBP formats.</li><br>
<li>Unique Identification: Uses enumerate to ensure filenames are unique and prevent overwriting.</li><br>
<li>Binary Processing: Downloads raw binary data via requests.content to ensure zero file corruption.</li><br>
</ul>
<h2>How to use</h2>
<h3>1. Prerequisites</h3>
<p>Ensure you have the necessary libraries installed:<br> `pip install requests beautifulsoup4` </p><br> 
