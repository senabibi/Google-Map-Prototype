<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/senabibi/PriorityQueue">
    <img src="https://github.com/senabibi/PriorityQueue/blob/main/maze.png" alt="Logo" width="500" height="400">
  </a>

  <h3 align="center">Priority Graph</h3>

  <p align="center">
    A Python implementation of a graph data structure with priority functionality. The project utilizes Dijkstra's algorithm to find the shortest path and provides a menu-driven interface for users to interact with the graph.
    <br />
    <a href="https://github.com/senabibi/PriorityQueue"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/senabibi/PriorityQueue">View Demo</a>
    ·
    <a href="https://github.com/senabibi/PriorityQueue">Report Bug</a>
    ·
    <a href="https://github.com/senabibi/PriorityQueue">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


## About The Project

![Priority Queue Flowchart](https://github.com/senabibi/PriorityQueue/blob/main/flowchartt.png)

The Priority Graph project is a Python implementation of a graph data structure with priority functionality. It provides methods for entering a city, listing the k closest cities, finding the shortest path to a destination city, and more. The graph is built using Dijkstra's algorithm, and the menu-driven interface allows users to interact with the graph seamlessly.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python.py]][Python-url]
* [![Vısual Studio Code][vsc.com]][VSC-url]
* [![BRAVE][brave.com]][BRAVE-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

This section provides instructions on how to set up and run the project locally. Please follow these steps to get your environment ready.

### Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

* [Python](https://www.python.org/downloads/): You'll need Python to run this project.


![Priority Queue Flowchart](None)

### Installation

Follow these steps to install and run the project:

1. **Python Installation:**
   - Download and install Python from the [official Python website](https://www.python.org/downloads/).



<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Usage
<div align=center>
    <img src="https://github.com/senabibi/PriorityQueue/blob/main/uml.png" alt="Priority Queue UML">

</div>

To use the Priority Graph project  and set up your work routine, follow these steps:

1. **Python Installation:**
   - Ensure that Python is installed on your system. If it's not already installed, you can download it from the [official Python website](https://www.python.org/downloads/).

2. **Creating the Graph:**
   -Run the script to initialize the Priority Graph.
    Vertices and edges will be added based on the data provided in the [my_graph](https://github.com/senabibi/PriorityQueue/blob/main/complex.py) variable.
     
 
3. **Menu-Driven Interface:**
   - Once the graph is set up, a menu-driven interface will be displayed.
     Options are available for entering a city, printing the current city, listing k closest cities, 
     finding the shortest path to a destination city, and exiting the interface.

4. **Entering a City:**
   - Choose option 'a' from the menu.
   - Enter the name of the city when prompted.
   - This sets the current city for subsequent operations.

5. **Printing Current City:**
   - Choose option 'b' to print the currently set city.
     If no city is set, a message indicating that the current city is not set will be displayed.
     
6. **Listing K Closest Cities:**
   - Choose option 'c' to list the k closest cities to the current city.
  Enter the value of k when prompted.
  The k closest cities will be displayed.

7. **Finding Shortest Path:**
   - Choose option 'd' to find the shortest path to a destination city.
   Enter the destination city when prompted.
  The shortest path from the current city to the destination city will be displayed.               

8. **Exiting the Interface:**
   - Choose option 'x' to exit the menu-driven interface and end the program.
    Feel free to explore and interact with the Priority Graph project, analyzing the graph's properties and performing various operations through the user-friendly menu-driven interface.
    


<p align="right">(<a href="#readme-top">back to top</a>)</p>





## Roadmap

- [ ] Python Installation: Ensure that you have the latest version of Python installed on your system for project development.
- [ ] Familiarize with Priority Graph Logic: Get acquainted with the logic behind the Priority Graph, including Dijkstra's algorithm for finding the shortest path and heap implementation for priority queue.
- [ ] Graph Implementation: Understand the structure of the provided Python script that implements the Priority Graph. Explore methods for entering a city, printing the current city, listing k closest cities, and finding the shortest path to a destination city.
- [ ] Graph Initialization: Run the script to initialize the Priority Graph with vertices and edges based on the data provided in the my_graph variable.

- [ ] User Interaction: Explore the menu-driven interface, allowing users to interact with the Priority Graph through options such as entering a city, printing the current city, listing k closest cities, finding the shortest path, and exiting the interface.

- [ ] Test and Debug: Thoroughly test the Priority Graph implementation, ensuring that each functionality works as expected. Address any issues or bugs that may arise during testing.
- [ ] Documentation: Document the Priority Graph project, providing a comprehensive guide on how to use each functionality and understand the underlying logic of the graph implementation.
This roadmap outlines the key steps to understand, interact with, and test the Priority Graph project. Follow these steps to explore the capabilities of the Priority Graph and gain insights into its functionality.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this project better, please fork the repository and create a pull request. You can also simply open an issue with the "enhancement" tag.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contact

Nursena Bitirgen - [LinkedIn](https://www.linkedin.com/in/nursena-bitirgen-5743341b9/)

Project Link: [https://github.com/senabibi/PriorityQueue](https://github.com/senabibi/PriorityQueue)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Acknowledgments

The development of the Priority Graph project was made possible thanks to various resources and skills:

* **Python Knowledge:** Special gratitude to the Python programming language for providing a robust and versatile foundation for this project.
* **Graph Algorithm Proficiency:** Acknowledgment to the understanding and implementation of essential graph algorithms, particularly Dijkstra's algorithm for finding the shortest path in a weighted graph.
* **Heapq Module Implementation:** Appreciation for the effective utilization of the 'heapq' module, which played a crucial role in implementing priority queue functionality.
* **Menu-Driven Interface Design:** Recognition for the development of a user-friendly menu-driven interface that allows users to interact with the Priority Graph seamlessly.

* **Data Structure Expertise:** Thanks to a solid understanding of data structures, particularly the implementation of a graph using dictionaries and the adjacency list representation.

* **Testing and Debugging:** Recognition for thorough testing and debugging efforts, ensuring the functionality and reliability of the Priority Graph in various scenarios.

* **Documentation:** Gratitude for creating comprehensive documentation that guides users on understanding and utilizing the features of the Priority Graph effectively.


The collaborative effort of these skills and resources contributed to the successful development of the Priority Graph project, providing a valuable tool for graph traversal and analysis.
<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/senabibi/PriorityQueue.svg?style=for-the-badge
[contributors-url]: https://github.com/senabibi/PriorityQueue/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/senabibi/PriorityQueue.svg?style=for-the-badge
[forks-url]: https://github.com/senabibi/PriorityQueue/network/members
[stars-shield]: https://img.shields.io/github/stars/senabibi/PriorityQueue.svg?style=for-the-badge
[stars-url]: https://github.com/senabibi/PriorityQueue/stargazers
[issues-shield]: https://img.shields.io/github/issues/senabibi/PriorityQueue.svg?style=for-the-badge
[issues-url]: https://github.com/senabibi/PriorityQueue/issues

[license-shield]: https://img.shields.io/github/license/senabibi/PriorityQueue.svg?style=for-the-badge

[license-url]: https://github.com/senabibi/PriorityQueue/blob/main/LICENSE

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/nursena-bitirgen-5743341b9/
[product-screenshot]: https://github.com/senabibi/PriorityQueue/blob/main/flowchartt.png

[Python.py]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://docs.python.org/3/



[vsc.com]: 	https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white
[VSC-url]: https://code.visualstudio.com/

[brave.com]:https://img.shields.io/badge/Brave-FF1B2D?style=for-the-badge&logo=Brave&logoColor=white
[BRAVE-url]: https://brave.com/





