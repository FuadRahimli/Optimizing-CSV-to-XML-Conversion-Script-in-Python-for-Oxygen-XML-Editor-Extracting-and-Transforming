I have developed a Python script based on the requirements specified by the product owner. The script is designed to process a CSV file containing a substantial dataset with more than 3000 rows. The goal is to convert all the data into a single XML file, presenting the information from each row in a specific style with designated tags.

It is imperative that the resulting XML file adheres to a common beginning, maintaining the prescribed format. Additionally, the order of columns in the CSV file must be rearranged in the XML file. To ensure compatibility with Oxygen XML Editor, the script has been developed with Oxygen's working principles in mind.

Addressing potential issues with error symbols present in the CSV file, I have implemented a systematic replacement approach to mitigate problems during XML file creation and operation in Oxygen. Specifically, the "xml.dom.minidom" library is utilized for XML file generation, and for enhanced performance in handling large XML documents, the script employs the "xml.etree.ElementTree" alternative library.

The script has been thoroughly tested and is executable in Visual Studio, demonstrating proper functionality in both Visual Studio and Oxygen XML Editor environments.

Achievements: 
Thanks to this task, I have honed a multitude of skills, including Python programming, Data processing, XML handling, Error management, Library utilization, Problem-solving, and Testing.
