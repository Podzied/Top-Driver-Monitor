# Top-Driver-Monitor
<h1 align="center">
  <br>
  Top Driver Monitor Documentation
</h1>
<h4 align="center">Be sure to :star: my configuration repo so you can keep up to date on any daily progress!</h4>
<div align="center">
  <h4>
    <a href="https://github.com/Podzied/Top-Driver-Monitor/commits/master"><img src="https://github.com/Podzied/Top-Driver-Monitor/commits/master"/></a>
        <a href="https://github.com/CCOSTAN/Home-AssistantConfig/commits/master"><img src="https://img.shields.io/github/commit-activity/y/CCOSTAN/Home-AssistantConfig.svg?style=plasticr"/></a>

  </h4>
</div>
<p><font size="3">
As many of you know I am currently a high school student studying computer science, along with that I need to complete drivers for my drivers education class in order to pass and get my drivers license. Because of this I created the Top Driver monitor. It is a monitor that continously checks TopDriver for any avalible drives. You can search by location, date, time, appointment type, pickup type, and many other filters. This is just one example of how I use programming in my daily life.</p>

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

</div>

