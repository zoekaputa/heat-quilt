# heat-quilt

### Heat Quilt is a data display of sexual crime in Seattle done for DXARTS 472: Mechatronic Art, Design, and Fabrication II.

### Project Description:

This project is a crochet quilt representing a data heat map, which is a data visulization technique that seperates data in subsections using two variables then displayes them in a grid. Rather than displaying data by color or shade, Heat Quilt uses heat to represent quanitites of data. The project is aimed to display data related to sexual violence in the city of Seattle along with examining our current state of data visulization and representation to find a more embodied and appreciative form of interacting with data.

This project first produces a heat map of particular offenses (Fondling, Sexual Assult with an Object, and Peeping Tom) in particular neigborhoods of Seattle (Roosevelt/Ravenna, Wallingford, University). This heat map is included as "heatmap_blanket.png" in the "arduino-code-and-cirucit" folder. Each bucket of this heat map is then compared to the average number of data present in a bucket. If any given bucket is higher than the average, the corresponding sqaure of the heat map blanket is also heated. If not, the corresponding sqaure is not heated.

Heat Quilt drew inspiration from the concepts of data humanism and data feminism, as discussed in Georigia Lupi's work Data Humanism: *The Revolutionary Future of Data Visualization* and Data Feminism as discussed in Catherine D'Ignazio and Lauren Klein's book *Data Feminism*. Data today is so far removed from embodiment, from the source it represents. By bringing physicality back to the numbers and categories of data, I mean to depart data from the human superiority that reigns over it.

This project aims to connect individuals with data on a level deeper than simple visualizations and question their experience with the quilt as a display of nearby sexual assult. Speculating at a possible future of data experiences, I have combined the personal aspects into this quilt in as many ways as possible. Yarn was bought locally, and the fringe of the quilt is made partly of disgarded clothing from myself, my friends, and my family. Further, the data I chose to display targets areas nearby to my current residence and the University of Washington. My choice in sexual offense data to explore an issue that is relevent to me, specifically as a woman in this area. Because quilts already have connotations of being homey and comforting, attaching data that is unpleasent and often involves negative physical touch provides an ambigous experience to the user. In this way, this project embodies the contact between self and data, which is often disturbingly unclear.

However, I'll also note that this project also expresses the limitations of data visulization and embodiment. The quilt does not focus on expressing the sexual assult data in an easily understandable way. Because of this, it's valid to say that the quilt "fails" to show or encompass the data. Actually interpreting the data by just experiencing the blanket is quite difficult. Althought this notion is amplified in this project, it exists in all data visulizations. Innately, summarizing data makes it ambiguous. This is an issue we will always encounter while analyzing data, and one we must work through by attempting new techniques.

For more details on the background of the original idea behind this work, reference the included Project Idea and Methodology pdf. Note that this project has far expanded from its orognal intention.

### Presentation:

In an ideal setting this work woud be displayed in a public space either on the ground or on a peice of furniture. Audience member will enter the installation with an understanding of the project: its name and the information being displayed in the heat map. They would have to oppertunity to touch, pick up, and cover themselves with the blanket. The video referenced in the Documentation section of this README would also play nearby the blanket (without sound). When leaving the exhibit, the audience will have access/be shown the computer generated heat map "heatmap_blanket.png" from the "arduino-code-and-cirucit" folder of this repository. The goal of this presentation is to allow the audience to explore the artwork from their own personal lens along with seeing my own view of it.

### References/Inspiration:

Wilkinson, L., & Friendly, M. (2009) The History of the Cluster Heat Map. *The American Statistician*, 63(2), 179-184. https://www.cs.uic.edu/~wilkinson/Publications/heatmap.pdf

Lupi, G. (2017a, January 30). Data Humanism: *The Revolutionary Future of Data Visualization*. PRINT. https://www.printmag.com/post/data-humanism-future-of-data-visualization

Urmila. (2021, February 19). *African American Writers* [data visualization]. Observable (n.d.). Retrieved from: https://observablehq.com/@urmilaj/african-american-writers

Lupi, G. (2017b, October 1). *Data Items: A Fashion Landscape at the Museum of Modern Art* [installation] Museum of Modern Art, New York City, New York. Retrieved from: http://giorgialupi.com/data-items-a-fashion-landscape-at-the-museum-of-modern-art

Rachel, N. (2011). Data Scarves [Clothing]. Cool Hunting (2011, December 19). Retrieved from: https://coolhunting.com/style/data-scarves/

D'Ignazio, C. & Klein L. F. (2020). *Data Feminism* The MIT Press

Psarra, A. & Varela, M. & Koutsomichalis, M. (2013). *Oiko-nomic Threads* [Textile] *Oiko-nomic Threads* Greek National Museum of Contemporary Art and the National Documentation Centre

Splan, L. (2016). *Embodied Objects* [Textile/Sculpture/Graphic] IMRC at The University of Maine Department of New Media, SIM Residency

Van Waardenberg, B. & Satomi, M. (2013). WS3.1: Building Heat Controlling Circuit [Workshop] ETextile Summer Camp. Retrieved from http://etextile-summercamp.org/2013/?p=540

City of Seattle. (2021). SPD Crime Data: 2008-Present [csv]. Retrieved from https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5


### Proof of Concept Prototype:

Heat Quilt began with construction of different forms of heat producing circuits. Various iterations and techniques used in this design can be referenced in the folder "heat-producuing-cirucit-design-archive". The inital design was using an embriodery machine to create a pattern with conductive thread. However, due to the lack of heat produced by the conductive thread used, this design was ineffective. The next and current design involved manually wrapping conductive thread around yarn. This produced a more effective heating mechanism. The current form of design is noted in this folder.

An arduino circuit supporting heating two sections on the quilt has been made, and the design of this circuit can be referenced in the folder "arduino-code-and-cirucit" along with the Arduino code supporting it. Note that the included sketch uses motors to represent the fabric "heating pads" created with conductive thread. Also note that an external 9V battery was used in this circuit, but the voltage of the battery used depends on the fabric "heating pads" created. As of now, this project is using an external supply of 9V (powered from a wall plug).

For a short video documentation of this froof of concept, see this youtube video: https://youtu.be/i5hmYlKIMhw.

### Documentation:

For docmentation of the production process, visit the photos in the "quilt-design-documentation" folder. Photos of the final quilt design are included in the "final-quilt-documentation' folder. For a video documentation of the aesthetic and spirit of this project, see this youtube video: https://youtu.be/Tr5On5pCPpQ.

### To Use:

Recreate the heat producing circuit FullArduinoCircuit.jpg as in "arduino-code-and-cirucit" and run the python script also in this folder.

FullArduinoCircuit.jpg is quite complex, but this circuit is similar to ArduinoCircuit.jpg, but just requires 9 heating elements rather than 2. The included sketch uses motors to represent the fabric "heating pads" created with conductive thread. Also, an external 9V battery was used in this circuit, but the voltage of the battery used depends on the fabric "heating pads" created. As of now, this project is using an external supply of 9V (powered from a wall plug).

Further, this python script is dependent on several installations; the pyfirmata, time, pandas, seaborn, and matplotlib libaraies.

And finally, the program is also dependent on the file SPD_Crime_Data__2008-Present.csv being present in the same folder as the code. This code was extracted from https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5 on June 5 2021. This file is too large to include in the repository, but you may extract the data manually from this website.

Note that this project requires care during setup and running considering it is using electronics and materials that can easily burn.
