# Top-Driver-Monitor
<h1 align="center">
  <a name="logo" href="https://www.vCloudInfo.com/tag/iot"><img src="https://gridfiti.com/wp-content/uploads/2020/06/Gridfiti_Blog_20-06_MacScreensavers_2_Analog.jpg" alt="Bear Stone Smart Home" width="200"></a>
  <br>
  Bear Stone Smart Home Documentation
</h1>
<h4 align="center">Be sure to :star: my configuration repo so you can keep up to date on any daily progress!</h4>
<p align="center"><a align="center" target="_blank" href="https://vcloudinfo.us12.list-manage.com/subscribe?u=45cab4343ffdbeb9667c28a26&id=e01847e94f"><img src="https://feeds.feedburner.com/RecentCommitsToBearStoneHA.1.gif" alt="Recent Commits to Bear Stone Smart Home" style="border:0"></a></p>
<div align="center">
  <h4>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig/stargazers"><img src="https://img.shields.io/github/stars/CCOSTAN/Home-AssistantConfig.svg?style=plasticr"/></a>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig/commits/master"><img src="https://img.shields.io/github/last-commit/CCOSTAN/Home-AssistantConfig.svg?style=plasticr"/></a>
        <a href="https://github.com/CCOSTAN/Home-AssistantConfig/commits/master"><img src="https://img.shields.io/github/commit-activity/y/CCOSTAN/Home-AssistantConfig.svg?style=plasticr"/></a>

  </h4>
</div>
<p><font size="3">
As many of you know I am. The configuration, devices, layout, linked Blog posts and YouTube videos should help inspire you to jump head first into the IOT world.  This is the live working configuration of <strong>my Smart Home</strong>. Use the menu links to jump between sections.  All of the code is under the <em>config</em> directory and free to use and contribute to.  Be sure to subscribe to the <a href="https://eepurl.com/dmXFYz">Blog Mailing list</a> and YouTube Channel. (https://YouTube.com/vCloudInfo)</p>
<div align="center"><a name="menu"></a>
  <h4>
    <a href="https://www.vCloudInfo.com/tag/iot">
      Blog
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#devices">
      Devices
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc">
      Todo List
    </a>
    <span> | </span>
    <a href="https://twitter.com/BearStoneHA">
      Smart Home Stats
    </a>
    <span> | </span>
    <a href="https://www.vcloudinfo.com/click-here">
      Follow Me
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig/tree/master/config">
      Code
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#diagram">
      Diagram
    </a>
    <span> | </span>
    <a href="https://youtube.com/vCloudInfo">
      Youtube
    </a>
    <span> | </span>
    <a href="https://amzn.to/2HXSx2M">
      Merch
    </a>
  </h4>
</div>

![Screenshot of Home Assistant Header](https://i.imgur.com/vjDH1LJ.png)

As of 2018, I have migrated everything to a Docker based platform.  You can read all about it here:
[Migration Blog Post](https://www.vCloudInfo.com/2018/02/journey-to-docker.html)
<hr>

#### <a name="software"></a>Notable Software on my Laptop Host:
* [Docker](https://Docker.com) - Docker runs on a Ubuntu Server Core base. [Video on Ubuntu Upgrades](https://youtu.be/w-YNtU1qtlk)
* [Youtube Video on Upgrading Home Assistant in Docker](https://youtu.be/ipatCbsY-54) - Be sure to Subscribe to get all Home Assistant videos.
* [Home Assistant Container](https://home-assistant.io/) - It all starts here.
* The amazing [Floorplan](https://github.com/pkozul/ha-floorplan) project to help visualize my smarthome.
* SSL via [SSLS](https://SSLS.com) - 5 Bucks A Year! - Keeps me safe! - [Youtube Video on Port Forwarding](https://youtu.be/y5NOP1F-xGU) - On my Arris TG1682 Modem
* [Docker-Compose.yaml](https://github.com/CCOSTAN/Docker_Support) - Realtime list of all the Containers.
* [Dasher Container](https://github.com/maddox/dasher) to leverage those cheap [Amazon Dash Buttons](https://youtu.be/rwQVe6sIi9w)
* [HomeBridge Container](https://github.com/nfarina/homebridge) for full HA <-> Homekit compatibility.
* [Unifi controller Container to manage](https://github.com/jacobalberty/unifi-docker) [APs](https://amzn.to/2mBSfE9)

![Screenshot of SmartHome](https://lh3.googleusercontent.com/-vKGF5gdz_VY/WVpP7qjsmjI/AAAAAAADVZ4/sGyiS1PjouUQxrEbWVfot6raxcElv4r-wCHMYCw/s1600/clip_image001%255B4%255D)
Lots of my gear comes from [BetaBound](https://goo.gl/0vxT8A) for Beta Testing and reviews.
Be sure to use the referral code 'Reliable jaguar' so we both get priority for Beta Tests!

#### <a name="diagram"></a>Smart Home Diagram - Get your icons (<a href="https://www.vcloudinfo.com/2018/07/the-bear-stone-home-assistant-icon.html">here</a>).
Here is how all the parts talk to each other.  Keep reading to see code examples and explanations.
![Smart Home Diagram](https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/bearstoneflow.png)

<p align="center"><strong>Smart Home diagram (<a href="https://pbs.twimg.com/media/Dg_CPwVU8AEyC2B.jpg:large"><code>PNG</code></a>). Made with <a href="https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=BearStoneFlow.xml#Uhttps%3A%2F%2Fraw.githubusercontent.com%2FCCOSTAN%2FDocker_Support%2Fmaster%2FBearStoneFlow.xml">Draw.io</a> (<a href="https://raw.githubusercontent.com/CCOSTAN/Docker_Support/master/BearStoneFlow.xml"><code>XML</code></a> source file).</strong></p>

<a name="devices"></a>
<div align="center">
  <h4>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#battery">
      Batteries
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#networking">
      Networking
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#alexa">
      Alexa
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#mobiledevices">
      Mobile Devices
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#nest">
      Nest
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#voice">
      Voice
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#hubs">
      Hubs
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#lights">
      Lights
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#switches">
      Switches
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#landscaping">
      Landscaping
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#LED">
      DIY LED Lights
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#garage">
      Garage
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#TV">
      TV Streaming
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#security">
      Security
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#cameras">
      Cameras
    </a>
    <span> | </span>
    <a href="https://github.com/CCOSTAN/Home-AssistantConfig#sensors">
      Sensors
    </a>
  </h4>
</div>

