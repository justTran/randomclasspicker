import random

theory_clist = ["15599	COT	4210	Automata Thry/Formal Languages	BSCS	Theory",
        "18171	COT	4521	Computational Geometry	        BSCS	Theory"]
hardware_clist = ["24483	CDA	4321    Cryptographic Hardware	        BSCS	Hardware",
        "18749	CDA	4621    Control of Mobile Robots	    BSCS	Hardware",
        "13595	CDA	4253	Field Prgm Gate Array Design	BSCS	Hardware",
        "12594	CAP	4401	Image Processing Fundamentals	BSCS	Hardware"]
software_clist = ["23670	COP	4710	Database Design	                BSCS	Software",
        "16799	COP	4365	Software System Development	    BSCS	Software",
        "17154	COP	4656	Software Devl Mobile Devices	BSCS	Software",
        "11058	CIS	4930	Capture the Flag	            BSCS	Software",
        "24481	COP	4620	Compilers	                    BSCS	Software",
        "18174	CIS	4930	Comp Methods for Imaging	    BSCS	Software",
        "13474	CIS	4930	Quantum Computing	            BSCS	Software",
        "15729	COP	4710	Database Design	                BSCS	Software",
        "22785	CIS	4930	Privacy-Preserving Infras.	    BSCS	Software"]

if not software_clist or not hardware_clist or not theory_clist:
    pass

else:
    elective_choice = input("Pick a elective type to get randomly assigned a class (theory, software, hardware): ")
    if (elective_choice == 'theory'):
        print("We selected this just for you")
        print(theory_clist[random.randint(0, len(theory_clist) - 1)])
    elif(elective_choice == 'hardware'):
        print("We selected this just for you")
        print(hardware_clist[random.randint(0, len(hardware_clist) - 1)])
    else:
        print("We selected this just for you")
        print(software_clist[random.randint(0, len(software_clist) - 1)])
        
