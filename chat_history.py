from haystack.dataclasses import ChatMessage, ChatRole
from typing import List
  
linkedin_chat_history = {
  "event": [
    ChatMessage(
      content="""
      Event Title: Cloud Native Computing Foundation (CNCF) Chennai - Oct 2024 Meetup
      
      Event Details: 
      
      Talk 1: "Preventing Lateral Movement Attacks on Cloud Services and Resources" by Midhun NS & Dhamupravin S, focused on critical cloud vulnerabilities and actionable solutions. 
      
      Talk 2: "What's Next in Kubernetes 2025?" by Ganesh Kumar Kasiviswanathan, introducing future trends like KubeVirt, Kubeflow for GenAI, and Compact Edge. Engaging discussions on cloud security, Kubernetes advancements, and the future of cloud-native technologies.
      
      Thanks Details: Thanks to Manikandan Krishnamurthy, Vijayabharathi Karuppasamy, Padmanaban Solaimalai, and YuniQ for organizing this enriching event. Special mention for the Kubernetes swag that added a fun touch!
      """,role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content=""" 
      Hi folks, 

      Had an amazing experience at the Cloud Native Computing Foundation (CNCF) Chennai - Oct 2024 Meetup yesterday!  It was an incredible learning experience filled with insightful talks on security attacks and kubernetes. Here are my key takeaways from two standout sessions:

      Talk 1: "Preventing Lateral Movement Attacks on Cloud Services and Resources"
      Speaker: Midhun NS & Dhamupravin S
      
      We dove into the serious (but often underestimated!) threat of lateral movement in cloud environments. Imagine attackers gaining initial access and then hopping across infrastructure undetected. This session highlighted the vulnerabilities enabling this kind of movement and offered practical, actionable tips for hardening cloud defenses. A crucial topic for anyone invested in cloud security!

      Talk 2: "What's Next in Kubernetes 2025 ?"
      Speaker: Ganesh Kumar Kasiviswanathan

      Ganesh shared some exciting trends in Kubernetes, including:
      - KubeVirt for future-proofing virtualization by running VMs alongside containers
      - Kubeflow for GenAI to support AI-powered applications on a cloud-native platform
      - Compact Edge for optimized, modern edge computing with Kubernetes


      Big thanks to Manikandan Krishnamurthy, Vijayabharathi Karuppasamy, and Padmanaban Solaimalai for organizing & co-ordinating and to YuniQ for partnering such an enriching event! 

      Making it even better with some awesome swag (Kubernetes socks! 🧦💙), it's always fun to bring a piece of the community home!

      Grateful for the opportunity to learn, connect, and stay on top of emerging tech trends and can't wait to attend more CNCF Chennai Meetups! 🚀

      #CloudNative #AI #TechInnovation #Learning #Innovation #CNCFMeetup #CloudNativeChennaiMeetUp #CNChennaiMeetUp #CNChennai #CloudNativeChennai #CNChennaiMeetup

      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Event Title: Grafana Labs & Friends Chennai Meetup
      Event Details: 
      Talk 1: "Performance Testing Your Observability Stack - K6 to Your Rescue" by Chandra Mohan Dhanasekaran, covering load testing and performance optimization.
      
      Talk 2: "Our Grafana Story: Insights and Innovations" by MANOJKUMAR G, showcasing real-world observability challenges and solutions.
      
      Talk 3: "Leveraging OpenTelemetry for Observability in Modern Applications" by Selvaraj Kuppusamy, with a practical demo on OTEL integration.
      
      A fun quiz on Grafana and K6, topped off with knowledge-sharing and community interaction.
      
      Thanks Details: Special thanks to Achanandhi M, Surbhi Gupta, and Rishi Agrawal for organizing and making the event memorable with engaging sessions and cool swags.
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      Hey friends! 👋

      I had the pleasure of attending the "Grafana Labs & Friends Chennai Meetup" yesterday, and it was an incredible learning experience filled with insightful talks on observability and performance testing. Here's a quick recap of the highlights:

      Talk 1: "Performance Testing Your Observability Stack - K6 to Your Rescue" 
      Speaker: Chandra Mohan Dhanasekaran, Senior Cloud Architect, Philips 

      Chandra Mohan walked us through how centralized observability saves time and resources. He introduced us to Grafana K6, an open-source tool for load testing, and demonstrated how it enhances performance testing in an observability stack. OpenTelemetry (OTEL) also played a key role in data collection and processing.

      Talk 2: "Our Grafana Story: Insights and Innovations"
      Speaker: MANOJKUMAR G, SRE Professional, IBM

      Manojkumar shared fascinating insights on observability, discussing how their infrastructure handles logs, metrics, traces, and profiling. He presented three major real-world challenges and their solutions using Grafana and AI. This talk was my personal favorite, and I'm planning to dive deeper into these insights in an upcoming blog post. Stay tuned!

      Talk 3: "Leveraging OpenTelemetry for Observability in Modern Applications"
      Speaker: Selvaraj Kuppusamy, DevOps Engineer, Grootan Technologies
      
      Selvaraj explored the immense potential of OpenTelemetry in modern applications, particularly in DevOps and development environments. His talk included a demo that showcased how OTEL can be integrated into observability strategies for enhanced application performance.

      A big shout-out to Rishi Agrawal for organizing a fun and challenging quiz on Grafana and k6! The room was buzzing with knowledge, and the quiz winner walked away with a JetBrains license. 🎉

      And yes, they also handed out some really cool hashtag#GrafanaSwags! 😍 It was such a nice bonus to walk away with swags along with all the knowledge.

      Huge thanks to Achanandhi M and Surbhi Gupta for organizing and coordinating this fantastic event. Looking forward to attending more meetups in the future! 🚀

      #Grafana #Observability #PerformanceTesting #OpenTelemetry #K6 #Community #TechMeetup #GrafanaSwag #GrafanaLabs #GrafanaMeetUp #ChennaiMeetUp
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Event Title: Cloud Native Computing Foundation (CNCF) Chennai Meetup
      Event Details: 
      Session 1: "Seamless Cloud Deployments Without the Kubernetes Complexity" by Lakshmi Narasimhan Parthasarathy, highlighting the power of Epinio.

      Session 2: "Portals vs. Platforms: What Do You Need?" by Ram Iyengar, clarifying the technical and business trade-offs.

      Session 3: "The Future with Vertex AI" by Rushabh Vasa, exploring Retrieval-Augmented Generation (RAG) and AI innovations.

      A well-rounded event emphasizing cloud-native technologies, business alignment, and AI-driven possibilities.
      
      Thanks Details: Thanks to YuniQ and Google Developers Group for their partnership in delivering this valuable learning experience.
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      Hey folks , 

      ✨ An Incredible Learning Experience at Cloud Native Computing Foundation (CNCF) Chennai Meetup! ✨

      Yesterday, I had the privilege of attending the Cloud Native Computing Foundation (CNCF) Chennai Meetup, and wow, what an insightful event it was! 🙌 It was packed with cutting-edge topics, brilliant speakers, and valuable takeaways. Here's a quick recap:

      🌟 Seamless Cloud Deployments Without the Kubernetes Complexity 
      💡 Speaker: Lakshmi Narasimhan Parthasarathy

      Lakshmi introduced Epinio, a powerful tool that simplifies cloud deployments by abstracting Kubernetes complexity. His approach struck the perfect balance between ease of use and maintaining control over infrastructure. This tool is a real game changer for teams aiming to optimize resource use without getting stuck in vendor lock-in or facing @Kubernetes' steep learning curve. 🚀

      🌟 Portals vs. Platforms: What Do You Need?
      💡Speaker: Ram Iyengar 

      Ram's session was incredibly insightful, clarifying the differences between portals and platforms. With real-world case studies, I learned how portals can enhance user experience while platforms offer greater flexibility and scalability. This was a great reminder of how important it is to align technical decisions with business goals. 💻🔍

      🌟 The Future with Vertex AI
      💡 Speaker: Rushabh Vasa

      Rushabh's session on Vertex AI and Retrieval-Augmented Generation (RAG) was simply mind-blowing. He showed how AI can transform businesses by combining generative AI with search capabilities to create more intelligent, context-aware applications. The potential here is limitless! 🧠🤖

      A huge thank you to YuniQ and Google Developers Group for partnering such an enriching event! 

      Grateful for the opportunity to learn, connect, and stay on top of emerging tech trends. Looking forward to applying these insights to future projects and can't wait to attend more CNCF Chennai Meetups! 💪✨

      #CloudNative #AI #TechInnovation #VertexAI #RAG #CloudDeployments #PortalsVsPlatforms #Networking #Learning #Innovation #CNCFMeetup #CloudNativeChennaiMeetUp #CNChennaiMeetUp #CNChennai #CloudNativeChennai
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Event Title: Gen AI Exchange Hackathon Roadshow - Chennai
      Event Details: 
      A Google I/O recap, introduction to Google Gemini AI, and hands-on with Google AI Studio.
      
      Highlights included hackathon insights, inspiring keynote by Rahul Ganapathy, and a deep dive into real-world AI applications.
      
      A fantastic opportunity to learn about cutting-edge Generative AI technologies and network with industry leaders.

      Thanks Details: A big thank you to Devfolio for organizing this insightful meetup and showcasing Gemini AI's capabilities.
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      Hey folks,

      🌟 Exciting Recap from the Gen AI Exchange Hackathon Roadshow - Chennai! 🌟

      This week, I had the pleasure of attending an incredible event packed with valuable insights and opportunities in the world of Generative AI.

      The session kicked off with a recap of Google I/O, followed by an introduction to the latest updates and innovations with Google Gemini AI. We explored the powerful capabilities of Google AI Studio, now enhanced with Gemini AI support.

      The highlight of the meetup was the deep dive into the Gen AI Exchange Hackathon. We learned about the hackathon's structure, team formation rules, journey, and the exciting incentives and perks awaiting the winners.

      A major highlight was the inspiring talk by Rahul Ganapathy, Co-founder & CEO of Atsuya Technologies. Rahul shared his journey of founding a startup, identifying problems, leveraging AI for solutions, and achieving success. His insights on real-world applications of Generative AI were truly eye-opening, and the Q&A session was a great way to wrap up the event.

      A big thank you to Devfolio for organizing this insightful meetup and for the opportunity to explore the new features of Gemini AI!

      Interested in tackling real-world business challenges with Generative AI? Check out the Gen AI Exchange Hackathon by Google here: https://lnkd.in/gpPRAF48

      #genaiexchangehackathon #chennairoadshow #generativeai #googleai #geminiai #geminiapi #techInnovation #startupjourney #AIApplications #Hackathon2024 #speakersession #sessions #meetups #devfolio #roadshows
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Event Title: Cloud Native Chennai - Aug 2024 Meetup
      Event Details: 
      Session 1: "Cloud Native Containers: Myth, Truth, or Marketing?" by Ram Iyengar, delving into container technologies and standards.
      
      Session 2: "Mastering Cluster Management with Anthos Service Mesh" by Arunkumar M. & Seetha, focusing on service mesh integrations.
      
      Session 3: "Firebase Genkit" by Ashutosh S. Bhakare, demonstrating AI embedding in Firebase applications.
      
      The event highlighted transformative tools and techniques in cloud-native computing and AI.

      Thanks Details: Grateful to CNCF Chennai and Vijayabharathi Karuppasamy for hosting this informative meetup and fostering community learning.
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      🌟 Cloud Native Chennai - Aug 2024 Meetup Recap 🌟

      I had an incredible time at the latest Cloud Native Chennai meetup, where we delved into some cutting-edge topics in cloud technology! 🚀

      Here's a snapshot of the fantastic sessions we explored:

      🔹 Ram Iyengar from the Cloud Foundry Foundation enlightened us with "Cloud Native Containers: Myth, Truth, or Marketing?" He covered everything from creating container images and OCI standards to exploring tools like buildkit and podman, and why Docker has gained such prominence. 🌐

      🔹 Arunkumar M. and Seetha from Presidio took us through "Mastering Cluster Management with Anthos Service Mesh." They provided an in-depth look at service mesh technology, its role in managing microservices communication, and practical strategies for integrating Anthos Service Mesh into cloud infrastructures. 🛠️

      🔹 Ashutosh S. Bhakare , GDE, gave a deep dive into Firebase with "Firebase Genkit." He showcased Firebase's capabilities for web and mobile apps and introduced Firebase Genkit, a powerful tool for embedding AI into Firebase applications. 🔥

      A huge shoutout to Cloud Native Computing Foundation (CNCF) Chennai for hosting such an insightful meetup and special thanks to Vijayabharathi Karuppasamy for organizing this stellar event! 🙌

      #CloudNative #Containers #ServiceMesh #Firebase #AI #TechMeetup #CloudComputing #Microservices #OpenSource #TechEvent #Containerization #OCIStandards #Podman #AnthosServiceMesh #FirebaseGenkit #DataEngineering #TechCommunity #CloudInfrastructure #DevOps #TechInnovation #SoftwareDevelopment #TechTalks #MeetupHighlights
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    )
  ],
  "blog": [
    ChatMessage(
      content="""Blog Title: From Newbie to Web Developer
      Blog: Starting out in web development can feel a bit like navigating a maze with no map. In my latest blog post, I share how I went from a complete newbie to building my own websites. I talk about the struggles I faced, the resources that helped me, and some tips that might make your path a bit smoother.
      Blog Link: Metta's Tech Bytes 🚀
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""Hey everyone! 🌟

      Starting out in web development can feel a bit like trying to navigate a maze with no map, especially if you think you're behind or unsure where to start. I totally get it—I began my journey in the second semester of my first year and felt pretty lost at times. 😅

      In my latest blog post, I share how I went from a complete newbie to building my own websites 🌐. I talk about the struggles I faced, the resources that helped me, and some tips that might make your path a bit smoother.

      Curious? 🤔 Check out my story and get some inspiration to kickstart your own tech journey! You can read the full post here: Metta's Tech Bytes 🚀

      Let's learn and grow together! If you have any questions or just want to chat about coding, feel free to reach out. 💬💻

      #WebDevelopment #CodingJourney #TechTips #MettaTechBytes
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""Blog Title: Enhancing CSS Skills Through Real-World Projects

      Blog: Learning CSS can be a lot of fun, especially if you're a beginner! In my latest blog post, I share how mimicking real-world websites helped me refine my CSS abilities. By working on similar projects, I steadily improved my CSS skills.
      
      Blog Link: https://lnkd.in/ga9fPGPc
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""Hey everyone! 🌟

      Learning CSS can be a lot of fun, especially if you're a beginner! I've found an exciting way to do it—by mimicking real-world websites. That's how I started creating my first modern UI and responsive websites. By working on similar projects, I steadily improved my CSS skills. 🎨✨

      In my latest blog post, I share how these projects helped me refine my CSS abilities and the key concepts I learned along the way. Curious to know more? 🤔

      Dive into my blog and see how you can enhance your CSS skills too! You can read the full post here: https://lnkd.in/ga9fPGPc🚀

      Looking forward to hearing your thoughts and experiences. Let's inspire each other on this coding journey! 💬💻

      #CSS #WebDevelopment #FrontendDevelopment #LearnToCode #BeginnerCoder #CodingJourney #WebDesign #ResponsiveDesign #TechLearning #CodeNewbie #MettasTechBytes #WebDev #HTML #CSSSkills #Programming #TechCommunity #WebDevProjects #CodeLife #TechInspiration #BuildWithCSS
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""Blog Title: Getting Started with Open Source

      Blog: I just wrote an article about my journey into the world of open source. If you're new to open source, check out these tips and resources to get started, including beginner-friendly repositories and more.

      Blog Link: https://lnkd.in/ghmRiJ6N
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""Hey folks !

      I just wrote an article about my journey into the world of open source, and I'm super excited to share it with you all! 🌟

      If you're new to open source like me, check out these tips and resources to get started. From joining mailing lists and IRC channels to contributing to some beginner-friendly repositories, there's something for everyone.

      Read more about it here: https://lnkd.in/ghmRiJ6N

      Let's dive into open source together and make a difference! 💻✨

      #OpenSource #TechCommunity #NewbieContributor #CodingJourney #TechTips #Programming #LearnToCode #DeveloperCommunity #Innovation #Collaboration #TechGrowth
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""Blog Title: The Evolution of Container Technology

      Blog: Have you ever wondered how container technology evolved? In my latest blog, I explore why containers are so powerful, how Docker revolutionized the industry, and the role of the Open Container Initiative.
      
      Blog Link: https://lnkd.in/d_u2RDq6
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""Hey everyone! 👋

      Have you ever wondered how container technology evolved to become such a game-changer in software development? 🚀

      From the early days of FreeBSD Jail to the impact of Docker, containers have completely transformed the way we build and deploy applications. 

      In my latest blog, I explore this journey and dive into why containers are so powerful, how Docker revolutionized the industry, and the role of the Open Container Initiative in standardizing it all. 🌐

      If you're into DevOps or just curious about the tech that's driving modern development, you'll want to check this out!

      🔗 Read the full blog here 
      https://lnkd.in/d_u2RDq6

      #Containerization #Docker #DevOps #Kubernetes #CloudNative #SoftwareDevelopment #TechInnovation #Microservices #OpenSource #CloudComputing
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""Blog Title: Exploring Containerization Tools Post-CNCF Meetup

      Blog: Inspired by a CNCF Meetup session, I wrote a blog about Docker's impact, why Podman is a secure alternative, and tools like Buildah and Kaniko for container builds.

      Blog Link: https://lnkd.in/gW_8zWrb
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""Hey everyone! 👋

      I recently had the chance to attend the Cloud Native Computing Foundation (CNCF) Chennai Meetup, and it was an eye-opener! 🌟 Ram Iyengar, the Chief Evangelist at Cloud Foundry Foundation, gave a brilliant talk on "Cloud Native Containers: Myth, Truth, or Marketing?" where he explored the evolution of container technology, from the early days to the rise of Docker and beyond.

      Inspired by his talk, I wrote a blog diving deeper into:
      -> The game-changing impact of Docker on software development.
      -> Why Podman is becoming the go-to secure alternative.
      -> Top open-source tools like Buildah, Kaniko, and more that are reshaping container builds.

      If you're into DevOps or just curious about the future of containerization, check it out! Let's keep the conversation going on how these tools can enhance security and streamline our workflows.

      🔗 Read the full blog here https://lnkd.in/gW_8zWrb

      #DevOps #Containerization #Docker #Podman #OpenSource #CNCF #CloudNative #SoftwareDevelopment #Containers #OpenSourceContainers #CNCFChennai #CNCFMeetUp
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""Blog Title: Rootless Containers for Enhanced Security
      
      Blog: My latest blog dives into what rootless containers are and why they're essential for secure operations. I also discuss tools like Podman and how to run containers safely.
      
      Blog Link: https://lnkd.in/dD8s6Dw7
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""Hey everyone! 👋

      We all know how powerful containers are, but did you know that running them with root privileges can expose your entire system to serious security risks? 😱 That's where rootless containers come in—a game-changer for enhancing security in your containerized environments. 🚀

      In my latest blog, I dive into:
      -> What rootless containers are and why they're essential for secure operations.
      -> How tools like Podman make rootless the default, providing a safer alternative to Docker.
      -> Practical tips on how to check and run containers without root privileges.

      If you're serious about securing your infrastructure, this is a must-read! 🔒

      🔗 Read the full blog here https://lnkd.in/dD8s6Dw7

      #ContainerSecurity #RootlessContainers #DevOps #Podman #Docker #CloudSecurity #Infrastructure #OpenSource #CyberSecurity
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""Blog Title: Observability: Beyond Monitoring
      
      Blog: In my latest blog, I break down observability, its key differences from monitoring, and the three pillars: Logs, Metrics, and Traces. I share my experience with tools like Grafana and Cribl.
      
      Blog Link: https://lnkd.in/gwBsxnxU
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""Hey folks,

      Ever wondered how tech giants keep their systems running smoothly? Or how you can make your projects rock-solid? The secret is Observability! 🔍

      In my latest blog, I break down:
      ♦️ What observability really means
      ♦️ The key differences between observability and monitoring
      ♦️ The three pillars: Logs, Metrics, and Traces
      ♦️ How to get started with the right tools and techniques

      ✨ Highlights:

      ♦️ Logs: Like debugging your code with detailed records.
      ♦️ Metrics: The performance stats of your application.
      ♦️ Traces: Following the path of requests through your system.

      I also share my personal experience with observability tools like Grafana, Prometheus, and Cribl, showing how they helped me monitor and optimize systems effectively. 📈

      🔗 Read the full blog here to learn how observability can give you superpowers for your code! 💪 https://lnkd.in/gwBsxnxU

      #Observability #SystemMonitoring #TechForBeginners #DevOps #TechInsights #DataDriven #TechJourney #Grafana #Prometheus #Cribl
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""Blog Title: Elevating Observability with Grafana
      
      Blog: I explore how Grafana transforms observability with stunning visualizations and unified data sources. From custom alerts to deeper insights, learn how Grafana can elevate your game.
      
      Blog Link: https://lnkd.in/gUKbnXCj
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""Hey friends! 👋

      Apologies for the delay, but I'm thrilled to finally share my latest blog post with you! 🎉 

      After spending the past few months diving into Grafana Labs, I'm excited to share how this powerful tool has transformed my approach to observability. 🚀

      Grafana isn't just another dashboard—it's a game-changer. From turning complex data into stunning visualizations to uniting various data sources into one seamless view, Grafana has become an essential part of my toolkit. 🌟

      Over the past few months, I've used Grafana to set up custom alerts, explore analytics, and gain deeper insights into system performance. It's been a fantastic journey, and I'm eager to share how you can make the most of Grafana for your own observability needs.

      Curious to see how Grafana can elevate your observability game? Check out my blog for tips and insights from my personal experience.

      Dive in here ( Read the full blog! ) : https://lnkd.in/gUKbnXCj

      Happy exploring!

      #Grafana #Observability #DataVisualization #Monitoring #Analytics #DevOps #SysAdmin #TechJourney #OpenSource #Metrics #Alerting #DashboardDesign
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""Blog Title: Setting Up Cribl and Grafana for Data Collection
      
      Blog: I just published a detailed guide on setting up Cribl and Grafana for data collection, processing, and visualization. This step-by-step guide covers building real-time monitoring dashboards.
      
      Blog Link: https://lnkd.in/gKHN_CQW
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""🚀 New Blog Post Alert! 🚀

      Hey folks! 🌟 

      I just published a detailed guide on Setting Up Cribl and Grafana for Data Collection, Processing, and Visualization📊.

      If you're curious about how to collect, process, and visualize system metrics using Cribl Edge, Cribl Stream, and Grafana, this is for you! Whether you're starting to explore observability or looking to streamline your data pipeline, this step-by-step guide has you covered. 💡

      🔗 Check it out and start building your own real-time monitoring dashboard today: https://lnkd.in/gKHN_CQW

      Feel free to drop your thoughts or questions in the comments! Let's dive into observability together! 🛠️✨ 

      #Observability #DataCollection #Grafana #Cribl #DataVisualization #Monitoring
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""Blog Title: Observability Insights from IBM at Grafana Meetup
      
      Blog: I attended the Grafana and Friends Meetup, where an IBM SRE shared how they tackle observability challenges with AI and Grafana. Read my detailed blog for all the insights.
      
      Blog Link: https://lnkd.in/gJT2kc35
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""Hey folks,

      Had an amazing time at the Grafana and Friends Meetup in Chennai, where I attended a standout session by MANOJKUMAR G, an SRE from IBM. His insights on how IBM tackles observability challenges using Grafana and AI were truly eye-opening

      From missing logs in centralized systems to alert fatigue, Manojkumar shared practical solutions IBM has implemented to keep their systems running smoothly. It was fascinating to see how they're leveraging AI and unified dashboards to streamline diagnostics and reduce noise in alerts.

      This session has definitely deepened my interest in observability, and I'm excited to explore more advanced tools like the #LGTM stack and Cribl in the coming weeks.

      If you're curious about how IBM is pushing the boundaries of system monitoring, I've shared a detailed blog with all the insights.

      Check it out! 👉 https://lnkd.in/gJT2kc35

      #IBM #Observability #Grafana #TechInsights #AI
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    )
  ],
  "experience": [
    ChatMessage(
      content="""
      Detail: 
      Shared an achievement of receiving a Letter of Appreciation for serving as the General Secretary of SAAS (Student Association and Arts Society) for the 2023-2024 academic year.

      Key highlights of the tenure include:
        Representing student voices to the university administration to address key concerns and improve the student experience.
        
        Co-organizing the 77th edition of Techofes, South India's largest cultural fest, which featured movie nights, concerts, workshops, and various activities.
        
        Supporting the team in organizing events like Utopia and Techofes, ensuring they were impactful and memorable for students.
        
        Gained experience in teamwork, decision-making, and resolving challenges while connecting with remarkable individuals.

      Preference: Demonstrated a strong preference for leadership and teamwork in enhancing campus life and organizing large-scale cultural events.
      
      Gratitude: Expressed heartfelt thanks to SAAS members for their support and to everyone who contributed to the success of this journey.
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Detail: 
      Described an exciting learning journey exploring the basics of Grafana, Cribl, and observability over a few days.
      
      Highlighted the effort to gain hands-on experience by signing up for a webinar, aiming to deepen understanding and apply the knowledge gained.
      
      Preference: Emphasized the importance of continuous learning, particularly in technical tools and observability systems.
      
      Gratitude: Showed enthusiasm and appreciation for the opportunity to expand skills and knowledge in a new domain.
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      Detail:
      Announced being offered a hybrid internship position at Invisibl Cloud after successfully completing a rigorous selection process, which included:
        A task submission.
        An interview call.
        An online technical interview.
        An HR interview.
        Expressed excitement about contributing to real-world projects and learning through practical experience.

      Preference: Demonstrated a strong interest in applying skills to impactful projects and gaining valuable industry experience.
      
      Gratitude: Expressed gratitude to Harish Ganesan, CEO and Co-Founder of Invisibl Cloud, for providing this career opportunity.
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      Detail: 
      Shared a detailed journey as the General Secretary of SAAS at College of Engineering Guindy (CEG), Anna University:
        Began with campaigning for elections, engaging with class representatives, and securing their trust to win the position.
        Focused on addressing student queries and collaborating with management to resolve issues.
        Successfully organized cultural events like Utopia (within a week of forming the Arts Society) and Techofes.
        Highlighted responsibilities in organizing events, seeking sponsorships, and coordinating a team of 25 members across 9 domains.
        Participated in multiple aspects of event planning, including marketing, technical design, human resources, and corporate relations.
        Gained valuable experience in decision-making, problem-solving, and teamwork during challenging moments.

      Preference: Demonstrated a passion for leadership roles, organizing large-scale events, and enhancing student life through collaborative efforts.

      Gratitude: 
      Thanked the team members, domain office bearers, and the university management for their support.
      
      Expressed deep gratitude for the opportunity to lead and grow through this remarkable journey.
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      Detail:
      Highlighted contributions to the development of various platforms for Techofes and SAAS:
        The Techofes website: Acknowledged the foundational work by the team in building the structure and functionalities.
        The Micro Event website: Recognized efforts in executing the project, adapting to feedback, and delivering a professional platform.
        The SAAS mobile application: Praised the seamless development and deployment of the app, ensuring event information was well-integrated with the backend.
      Emphasized the role of collaboration and mentorship in delivering these projects successfully.
    
      Preference: Valued teamwork, web development, and the enhancement of user interfaces to create impactful and functional platforms for cultural and student association events.

      Gratitude:
      Expressed heartfelt thanks to:
        Team members for their dedication, hard work, and professionalism.
        Mentors for their guidance and support throughout the development process.
      Acknowledged the collective effort that brought these projects to life and ensured their success.
      """, role=ChatRole.USER, name="Metta"
    ),
  ],
  "contribution": [
    ChatMessage(
      content="""
      Details: Powering Through Long-Term Project Execution - A Notion template to help manage long-term projects with roles, objectives, milestones, and tasks.
      
      Link: https://lnkd.in/gv9kAZ_g
      
      Type of Contribution: Free Notion Template for Project Management
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      🚀 New Notion Template Alert! 🚀

      I'm excited to share my latest template: Powering Through Long-Term Project Execution ! 

      This template is designed to help you manage long-term projects with ease and efficiency.

      💼 Whether you're leading a team or tackling a big project solo, this template has you covered. From assigning roles and setting clear objectives to tracking milestones and breaking down tasks, it's all about keeping things organized and on track.

      ✨ It's free, and perfect for keeping everything running smoothly from start to finish! ✨

      Check it out here: 🔗 https://lnkd.in/gv9kAZ_g

      Let me know if it helps power up your projects! 💪

      #ProjectManagement #NotionTemplate #LongTermProjects #TeamCollaboration #MilestoneTracking #ProductivityBoost #ProjectPlanning #FreeTemplate #Notion
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Details: Structured API Documentation - A Notion template to simplify API documentation with clear organization for request limits, versioning, and object details.
      
      Link: https://lnkd.in/gzuwXtpF
      
      Type of Contribution: Free Notion Template for API Documentation
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      Hey folks, exciting news! 🚀

      I've just dropped a fresh Notion template designed to take the headache out of writing API documentation! 😄

      Introducing “Structured API Documentation” – your go-to guide for creating clear, organized API docs that developers will actually enjoy reading and using. Whether you're setting request limits, handling versioning, or detailing objects, this template keeps everything simple and accessible.

      ✨ It's free and ready to streamline your API workflow! ✨

      Curious? Grab it here: 🔗 https://lnkd.in/gzuwXtpF

      Let me know how it works for you! 🙌

      #APIDocumentation #NotionTemplate #DevCommunity #TechTips #CodingEssentials #APIIntegration #Notion #FreeTemplate
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Details: Open Source Contributions and Tools - A Notion page for contributing to open-source projects, mastering version control with Git, and optimizing workflows using GUI and command-line tools.
      
      Link: https://lnkd.in/gGj8DyhB
      
      Type of Contribution: Open Source Resource Hub
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      Hey folks!

      I'm excited to share a valuable resource I've put together for anyone interested in diving into the open-source world. Whether you're looking to contribute to open-source projects, master version control with Git, or streamline your workflow with GUI and command-line tools, this Notion page has got you covered!

      🔹 Open Source Contributions: Find out how you can get involved and make a difference. 
      🔹 Version Control & Commands: Master the essentials of Git and version management. 
      🔹 GUI & Command-Line Tools: Optimize your development workflow with the right tools.

      Explore this hub to enhance your open-source journey and coding efficiency. 

      Check it out and let's grow together in the open-source community! 🌍💪
      https://lnkd.in/gGj8DyhB

      #OpenSource #VersionControl #Git #DevelopmentTools #Coding #TechCommunity #Notion #OpenSourceContributions
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Details: Metta's Templates - A GitHub collection of template repositories with structured documentation and learning resources for coding projects.
      
      Link: https://lnkd.in/gaCVRgwF
      
      Type of Contribution: GitHub Templates for Developers
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      Coding a repository from scratch can be a daunting task for many of us. 

      Good documentation and structured templates are in high demand and incredibly useful for kickstarting projects. 

      That's why I created -> "💡Metta's Templates" 

      I've starred all my GitHub Template repositories
      - which are free, 
      - come with structured documentation, 
      - and include learning resources to help you get started quickly and efficiently.

      Check out Metta's Templates and elevate your next project with a solid foundation: https://lnkd.in/gaCVRgwF

      #GitHubTemplates #DeveloperTools #OpenSource #WebDevelopment #SoftwareEngineering #CodingMadeEasy #TechTemplates
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Details: Node Express Backend Template Using Prisma - A template for backend development with Prisma ORM, Node.js, and Express.js, featuring middleware, scalable architecture, and well-organized code.
      
      Link: https://lnkd.in/gbQgujsj
      
      Type of Contribution: GitHub Backend Development Template
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      Unlock the Power of Prisma ORM with my new Backend Template! 🚀

      Hey everyone! 🌟

      I'm thrilled to share the Node Express Backend Template Using Prisma, crafted to streamline your backend development with Prisma ORM.

      Whether you're a developer, student, or part of a team, this template is your gateway to building robust and scalable applications effortlessly.

      What's Inside? 🎁
      - Seamless Prisma ORM Integration for efficient database management 🗃️
      - Pre-configured Node.js and Express.js Setup for a quick start 🛠️
      - Essential Middleware for secure authentication and validation 🔐
      - Well-Organized Code Structure to keep your project tidy 🗂️
      - Perfect for anyone looking to kickstart their backend projects with a solid foundation. 

      Dive into the repo and let's build something amazing together !!!

      Repo link is here : https://lnkd.in/gbQgujsj

      Happy coding 🎉

      #Prisma #NodeJS #ExpressJS #BackendDevelopment #OpenSource #WebDevelopment #TechTemplates #SoftwareEngineering #Coding #DatabaseManagement #DevelopmentTools #TechCommunity
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Details: Node.js & Express.js Backend Template for Beginners - A GitHub repository with beginner-friendly tools, clear documentation, and a structured foundation for backend projects.
      
      Link: https://lnkd.in/gcDti_ZA
      
      Type of Contribution: Beginner-Friendly Backend Development Template
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      Hey friends! 🌟

      I'm thrilled to share a new project that I've been working on! 🎉 I've just created a new GitHub repository: Node.js & Express.js Backend Template for Beginners! 🚀

      This template is crafted specifically for those of you who are diving into backend development. It's designed to help you get started with ease and confidence. Here's what makes it stand out:

      📖 Clear Documentation: Easy-to-follow instructions to get you up and running quickly.
      🛠️ Essential Tools: Everything you need to build scalable and efficient applications is right here.
      📚 Structured Foundation: A solid base to help you understand and implement best practices.
      🔧 Best Practices: Follow industry standards to write clean and maintainable code.

      Whether you're just starting out or looking to polish your skills, this repo is here to guide you every step of the way. Check it out, explore, and let me know your thoughts!

      If you find it helpful, don't forget to ⭐️ star the repo and share it with others who might benefit from it!

      Repo link is here : https://lnkd.in/gcDti_ZA

      Happy coding! 💻✨


      #NodeJS #ExpressJS #BackendDevelopment #OpenSource #TechForBeginners #GitHub #CodingJourney #SoftwareDevelopment #WebDevelopment
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Details: Node Express Backend Template for Intermediates - A template for intermediate learners featuring Node.js, Express.js, Sequelize ORM, middleware, and a scalable architecture.

      Link: https://lnkd.in/eApX4Cw6
      
      Type of Contribution: Intermediate-Level Backend Development Template
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      🎉 Hey, everyone! I'm excited to share something I've been working on—my new Node Express Backend Template for Intermediates GitHub repository! 🌟

      If you're an intermediate learner with a basic understanding of backend development, this template is perfect for you! It's packed with everything you need to streamline your project setup and follow best practices

      This template is designed to help you level up your backend projects with a solid, scalable structure. I've made sure to include detailed documentation to guide you along the way.

      What's Inside?
      - Pre-configured setup for Node.js with Express.js
      - Database integration using Sequelize ORM
      - Essential middleware for authentication, validation, and more
      - Scalable and maintainable architecture
      - Detailed documentation to guide you through each step

      But don't worry, beginners—I haven't forgotten about you! 😉 I'm working on another repository with more detailed documentation and beginner-friendly content. Stay tuned; it's coming soon!

      Check out the Node Express Backend Template for Intermediates here: https://lnkd.in/eApX4Cw6

      I hope this template helps you in your learning journey. Let's keep building and growing together! 🚀

      #BackendDevelopment #NodeJS #ExpressJS #Sequelize #OpenSource #WebDevelopment #LearningJourney #GitHub #CodeNewbie #Developers #TechCommunity
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Details: ExpressJS API Boilerplate - A fully documented, beginner-friendly template for building APIs with Express.js, including modular structure and test cases.
      
      Link: https://lnkd.in/gXgBcWKK
      
      Type of Contribution: GitHub ExpressJS API Boilerplate
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""🚀 Hey Developers! 🌟

      Are you just starting out with Express.js and looking for a solid foundation to build your applications? 🤔 I've got something exciting for you!

      Introducing the ExpressJS API Boilerplate – a fully documented and beginner-friendly template to kickstart your Express.js projects. 🎉

      ✨ Why you'll love it:

      Comprehensive Documentation: Clear, well-organized comments and documentation to guide you every step of the way.

      Modular Structure: A clean setup with controllers, routes, and validators to keep your code maintainable and scalable.

      Test Cases Included: Ready-to-use test cases to help you ensure your API works as expected.

      🔗 Link to the repo : https://lnkd.in/gXgBcWKK

      Whether you're a newbie or just need a reliable template, this boilerplate is here to help you get up and running with Express.js effortlessly. Dive in, explore, and start building amazing APIs with confidence! 🚀

      Feel free to ⭐️ this repo if you find it useful, and 🍴 fork it to customize and contribute. And if you'd like to support my work, check out the Sponsor Me section in the repo!

      Happy coding! 💻💡

      #ExpressJS #WebDevelopment #API #OpenSource #TechCommunity #BeginnerFriendly #JavaScript #NodeJS #DeveloperTools #Programming #Coding #SoftwareEngineering #TechForGood #LearnToCode
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Details: Entry-Level Tech Resume Template - A Notion template designed for tech students to organize contact info, education, certifications, work experience, and projects in a professional format.

      Link: https://lnkd.in/gB3ebGgj
      
      Type of Contribution: Free Notion Resume Template
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      🚀 Exciting News for Tech Freshers! 🚀

      I'm thrilled to share my new “Entry-Level Tech Resume” template on Notion, designed specifically for tech students. This free template helps you organize your contact info, education, certifications, work experience, and projects in a professional format. It was incredibly helpful for me and even got filtered through resume filters!

      Access the free template here 🔗 https://lnkd.in/gB3ebGgj

      Feel free to use it and make your resume stand out! 😊

      #TechCareers #ResumeTemplate #Freshers #Notion #TechJobs #CareerAdvice #JobSearch #NewGrad #ResumeTips #TechStudents #CareerGrowth
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Details: Full Stack Development Roadmap 2024 - A roadmap outlining key skills, technologies, and trends to focus on for success in full-stack development in 2024.
      
      Link: Not Provided
      
      Type of Contribution: Roadmap for Full Stack Development
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      Excited to share the roadmap for Full Stack Development in 2024!

      The future of full stack development looks promising, and it's crucial to stay ahead of the curve. 🚀 Here's a comprehensive roadmap outlining the key skills, technologies, and trends to focus on for success in the year 2024. Let's dive in and pave our way to becoming top-notch full stack developers! 💪

      #fullstackdevelopment #techtrends2024 #roadmaptosuccess #FullStackDeveloperRoadmap #futureskills #techtrends2024 #stayahead
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
  ],
  "certificate": [
    ChatMessage(
      content="""
      Certificate Name: Introduction to Data Engineering on Azure
      Details:
        Issuing Authority: Microsoft Learn
        This course covered the essentials of data engineering on Azure, including building data pipelines, managing and transforming data, designing and implementing data storage solutions, and understanding data security and compliance.
      Link: Not Provided
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      🎉 Certification Earned: Introduction to Data Engineering on Azure
      Issuing Authority: Microsoft Learn

      I'm thrilled to share that I've completed the Introduction to Data Engineering on Azure! This course covered the essentials of data engineering on the Azure platform, from building data pipelines to managing and transforming data.

      Takeaways:
      🔹 Learned to design and implement data storage solutions on Azure
      🔹 Explored data processing and transformation using Azure services
      🔹 Gained insights into data security and compliance on the cloud

      This journey has deepened my understanding of how data can be stored, processed, and managed effectively in a cloud environment. I'm excited to bring these skills into future projects! Hope this inspires others to start their own @MicrosoftLearn journey 🚀

      #DataEngineering #MicrosoftAzure #CloudComputing #DataTransformation #LearningJourney
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Certificate Name: Complete Node.js Developer Course
      Details:
        Issuing Authority: Udemy
        The course covered the full scope of Node.js development, including Node.js fundamentals, backend principles, working with Express.js, MongoDB for data storage, and WebSocket for real-time features. It emphasized creating full-stack applications and integrating databases.
      Link: Not Provided
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      📜 Certification Earned: Complete Node.js Developer Course
      Issuing Authority: Udemy
      Certificate Link (optional): Certificate Link

      Excited to have completed the Complete Node.js Developer Course on Udemy! This course covered the full scope of Node.js development, from basic setups to advanced features.

      Course Highlights:
      🔸 Introduction to Node.js fundamentals and backend development principles
      🔸 Working with Express.js to create powerful web applications
      🔸 Building with MongoDB for data storage and WebSocket for real-time features

      Key Takeaways:
      🔹 Developed a deep understanding of the Node.js runtime and its ecosystem
      🔹 Practiced creating full-stack applications and integrating databases
      🔹 Enhanced my problem-solving skills and gained a new perspective on backend programming

      This certification has equipped me with the skills to build scalable and real-time server applications, and I'm excited to see where this knowledge takes me next! 💪

      #NodeJS #BackendDevelopment #WebSocket #MongoDB #JavaScript #Udemy
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Certificate Name: MERN Bootcamp
      Details:
        Issuing Authority: Udemy
        This intensive course provided a comprehensive understanding of the MERN stack (MongoDB, Express, React, Node.js). It included secure authentication with JWT, building and testing REST APIs with Postman API, and managing databases and RESTful architecture.
      Link: Not Provided
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      💥 Certification Earned: MERN Bootcamp
      Issuing Authority: Udemy
      Certificate Link (optional): Certificate Link

      Proud to announce the completion of the MERN Bootcamp on Udemy! This intensive course covered the entire MERN (MongoDB, Express, React, Node) stack, providing a thorough understanding of how to build full-stack applications from scratch.

      Course Highlights:
      🔹 Comprehensive overview of MongoDB, Express, React, and Node.js
      🔹 Using JSON Web Tokens (JWT) for secure authentication
      🔹 Building and testing REST APIs with Postman API

      Key Takeaways:
      ✅ Developed hands-on experience in building interactive full-stack applications
      ✅ Enhanced my understanding of managing databases and RESTful architecture
      ✅ Improved proficiency in building, testing, and debugging large web applications

      This journey through the MERN stack has been invaluable, and I'm excited to continue developing powerful, scalable web applications! 🎉

      #MERNStack #FullStackDevelopment #JavaScript #ReactJS #WebDevelopment #Udemy
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Certificate Name: Complete JavaScript Course
      Details:
        Issuing Authority: Udemy
        The course explored JavaScript fundamentals, advanced OOP techniques, manipulating the DOM for dynamic applications, and using REST APIs, JSON, and debugging tools. It focused on creating interactive and data-driven applications.
      Link: Not Provided
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      📘 Certification Earned: Complete JavaScript Course
      Issuing Authority: Udemy
      Certificate Link (optional): Certificate Link

      Thrilled to complete the Complete JavaScript Course on Udemy! This course provided an in-depth exploration of JavaScript, covering everything from basics to advanced programming concepts.

      Course Highlights:
      🔸 JavaScript fundamentals and advanced OOP techniques
      🔸 Manipulating the Document Object Model (DOM) for dynamic front-end applications
      🔸 Using REST APIs, JSON, and debugging tools to create responsive applications

      Key Takeaways:
      ✨ Strengthened my knowledge of JavaScript and its frameworks
      ✨ Learned how to implement object-oriented design in JavaScript projects
      ✨ Gained the confidence to create interactive, data-driven applications

      This course has been a game-changer, and I'm ready to dive into more challenging projects. Can't wait to see where this knowledge leads! 🌐

      #JavaScript #WebDevelopment #FrontEndDevelopment #OOP #Udemy
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Certificate Name: Responsive Website using HTML and CSS
      Details:
        Issuing Authority: Udemy
        The course covered HTML5 and CSS3 for building web layouts, implementing CSS Flexbox, CSS Grid, and Bootstrap for responsiveness, and best practices for front-end development and collaboration. It emphasized creating mobile-friendly web designs.
      Link: Not Provided
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      🌐 Certification Earned: Responsive Website using HTML and CSS
      Issuing Authority: Udemy
      Certificate Link (optional): Certificate Link

      Proud to share that I've completed the Responsive Website using HTML and CSS course on Udemy! This course covered the essentials of creating adaptable, responsive web layouts that provide a seamless user experience across devices.

      Course Highlights:
      🔹 Understanding HTML5 and CSS3 for building structure and styling
      🔹 Implementing CSS Flexbox, CSS Grid, and Bootstrap for responsive designs
      🔹 Learning best practices for front-end development and collaboration

      Key Takeaways:
      💡 Gained hands-on experience in creating mobile-friendly web designs
      💡 Improved my understanding of layout structuring with CSS Grid and Flexbox
      💡 Acquired practical knowledge in front-end technologies for modern web development

      I'm excited to continue refining my design skills and creating engaging, accessible web experiences. 💻

      #ResponsiveDesign #CSS3 #HTML5 #FrontEndDevelopment #WebDesign #Udemy
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    )
  ],
  "hackathon": [
    ChatMessage(
      content="""
      Name: Hackz'24 - Ideathon

      Purpose: To develop a solution addressing customer service issues in the fintech industry.

      Details:
      Hosted by CSEA_CEG, the solution aimed at improving customer service by creating a Customizable Multilingual AI Chatbot called INFINSA BOT.
      
      Features include multilingual and context-aware responses, image processing capabilities, customizable workflows, a learning mode for continuous improvement, and real-time data privacy and security compliance.
      
      The team conducted extensive research and multiple iterations, from brainstorming ideas to crafting a Figma prototype, presentation, and explanation video.
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      Hey folks!

      I'm excited to share that we've officially submitted our solution for Round 1 of the Hackz'24 - Ideathon! hosted by CSEA_CEG 🎉 

      It's been a fantastic journey collaborating with my talented teammates – Harini S., Adithyan, and Sundhar Balamoorthy – who brought their creativity, dedication, and skills to bring our idea to life.

      Among the tracks, we chose fintech, believing it has vast potential to explore and innovate. After deep research, we identified a key problem in customer service within the financial world — where traditional chatbots with scripted responses often fall short in addressing complex customer needs, resulting in frustration and high operational costs.

      Our solution? A Customizable Multilingual AI Chatbot - INFINSA BOT designed to transform customer service by:

      🌐 Providing Multilingual and Context-Aware Responses
      📷 Including Image Processing Capabilities
      🔧 Offering Customizable Workflows for tailored user experiences
      📈 Featuring a Learning Mode for continuous improvement
      🔒 Ensuring Real-Time Data Privacy and Security Compliance

      The journey began with brainstorming ways to boost customer engagement, enhance user satisfaction, reduce the demand for traditional customer support, and elevate user experience. From diving into LLMs, AI frameworks, and customer service challenges to researching existing solutions, we worked through multiple iterations, encountered a few roadblocks, and ultimately crafted a solution we're proud of. 

      With everything in place, we crafted a presentation, built a Figma prototype, and recorded an explanation video. After rounds of feedback and revisions, we wrapped it all up and submitted it! ✅

      Excited to see where this journey takes us next! 🚀

      #Hackz #Hackz24 #FintechInnovation #AIChatbot #Teamwork #CustomerExperience #Fintech #CSEACEG #CSEA
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Name: SIH 2024

      Purpose: To build a Conversational Image Recognition Chatbot for Bharat Electronics Limited (BEL).

      Details:
      The challenge involved developing a chatbot capable of detecting objects in images and engaging in a contextual conversation about them, with grammatically correct responses.

      The team learned about image recognition, object detection, LLMs, and AI frameworks, refining their solution through multiple revisions.

      The final deliverable included a presentation, explanation video, and submission after rounds of feedback and revisions.
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      Hey friends! 🌟

      I'm excited to share that we've officially submitted our solution for SIH 2024 ! 🎉 It's been a fantastic journey working with my amazing teammates – Harini S, Raja S, Dinesh Kumar, Shazz Abdul Samed, and Himanesh Venkatesan – who brought their dedication and skills together to complete this idea solution.

      We tackled the problem statement SIH1603 - Conversational Image Recognition Chatbot, provided by Bharat Electronics Limited (BEL). The challenge was to build an image recognition chatbot capable of detecting objects in images, having a contextual conversation about them, and generating grammatically correct responses based on the sender's messages. Quite the task, right?

      The journey began by filtering through various software problem statements that piqued our interest. After much discussion, we chose this one for its complexity, exciting use of emerging technologies, and overall challenge. 💡

      From learning about image recognition, object detection, LLMs, and various AI frameworks, to researching existing solutions, we worked through multiple revisions, encountered some roadblocks, but ultimately crafted a solution we're proud of. With everything in place, we worked on crafting a presentation and explanation video. After several rounds of feedback and revisions, we wrapped it up and hit submit! ✅

      Looking forward to seeing where this takes us! 🚀 

      #SIH2024 #Innovation #Teamwork #AI #Hackathon #AIChatBot #SmartIndiaHackathon #SmartIndiaHackathon2024
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    )
  ],
  "project": [
    ChatMessage(
      content="""
      Name: Techofes Backend API
      
      Purpose: To develop the backend for the Techofes website, integrating user-facing and admin-facing features.
      
      Details: Designed a robust database schema in PostgreSQL, integrated with Node.js and React.js. Created 
      two API routes: one for website users to display information and another for admins, allowing real-time fest monitoring via a mobile app. The API is preparing for live deployment.
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      🚀 Exciting News! 🚀

      Thrilled to announce the completion of the backend work for the Techofes Website! 🌐 Techofes, the grand cultural fest of College of Engineering, Guindy, Anna University Chennai, holds a special place in my heart , conducted by Student Association and Arts Society. 🎉

      This project began with a basic backend structure initiated by my senior, and I took it to the next level by designing a robust database schema and implementing it in PostgreSQL. 🛠️ The Techofes API, powered by Node.js, seamlessly integrates with React.js on the frontend.

      The API boasts two key routes: one catering to website users with information beautifully displayed on the Techofes website, and the other exclusively for admins. The admin route, connected to a mobile app, empowers them to monitor the fest in real-time, right from their smartphones! 📱

      I'm ecstatic to share that this API is gearing up to go live soon! 🚀 Stay tuned for more updates, and a huge shoutout to the incredible team behind this journey. 🙌🏼 Feeling accomplished and excited about what's to come! 🚀🌟

      #AnnaUniversity #CulturalFestivals #Techofes #BackendDevelopment #NodeJS #ReactJS #TechMilestone #PostgreSQL
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Name: Kurukshetra Admin API
      
      Purpose: To develop the backend for the admin API of the Kurukshetra tech fest, ensuring structured and efficient data management.
      
      Details: Implemented controllers, models, and routes with ordering, filtering, and sorting functionalities using TypeScript, PostgreSQL, and TypeORM. The API is in the staging and deployment phase, showcasing scalability and robustness.
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      I myself and my friend Raja S have been working tirelessly on the backend of the "Admin API" for Kurukshetra, a national level tech fest of College of Engineering, Guindy ✨ organized by CEG Tech Forum .

      🚀💻In the past few weeks, We've implemented controllers, models, and routes to showcase the raw data in the database in a structured way. But that's not all, folks! We also incorporated ordering, filtering, and sorting functionalities to make navigating the table data a breeze. 📊

      The tech stack we used for this project is an absolute powerhouse! 🚀🔥 We leveraged the power of TypeScript, ensuring a seamless and efficient API. 🌟 We also utilized PostgreSQL and TypeORM to handle the data storage and retrieval. These technologies have proven to be robust, reliable, and scalable, making them perfect for a project of this magnitude. 💯🔧

      We're thrilled to announce that the development of the API and its frontend is now complete, and we have moved into the staging and deployment phase. 🎉🚀 It's incredible to see everything coming together and witnessing the transformation of our hard work into a tangible product 💡.


      #TechFest #TechCommunity #Kurukshetra #BackendDevelopment #TypeScript #PostgreSQL #TypeORM #staging #deployment #annauniversity #ctf #cegtechforum
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Name: Met-Movie-API
      
      Purpose: To build a scalable data pipeline and API for enriched movie data management.
      
      Details: Extracted movie data starting with 'S' and 'H' from websites and APIs like IMDb and TMDB. Designed an ETL pipeline with Python, storing 10,000+ records in PostgreSQL. Developed a Flask-based API for seamless interaction with the database. Utilized Docker for deployment and scalability.
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      🚀 Exciting Announcement guys, a Data Engineering task conquered! 🎉

      I've successfully completed a challenging data engineering task 🤘 , and here's what it entailed:
      - To collect movie details starting with the letters 'S' and 'H' from at least two websites.
      - Leveraged any language of choice to scrape data from diverse sources like Wikipedia, IMDb, and Rotten Tomatoes.
      - Utilized middle layer APIs found on the web for streamlined data retrieval.

      🛠️ After crafting a schema tailored to store relevant movie details in a database of choice, I ensured scalability by populating the datastore with over 10,000 records.

      ✨ Data Pipeline Creation: Employed the ETL (Extract, Transform, Load) process in Python.
      - Extracted data seamlessly from the TMDB Movie API.
      - Transformed and enriched the data to suit the database schema.
      - Loaded the transformed data into a PostgreSQL database, meticulously designed by yours truly.

      🌐 I also developed the Met-Movie-API, a Python Flask service that allows users to access all the enriched movie data stored in the PostgreSQL database. The seamless integration enables users to interact with the database effortlessly.


      📚 Throughout this journey, I've acquired valuable skills. I mastered the ETL model, gained expertise in creating APIs using Flask for seamless data access, implemented multiprocessing techniques in Python for enhanced performance, and containerized the entire application for easy deployment and scalability using Docker.

      💼 I'm thrilled to invite you to explore the project on GitHub and contribute your insights and expertise.
      Let's collaborate and innovate together!

      GitHub Repo: https://lnkd.in/gXFf-8gX

      #DataEngineering #ETL #Python #FlaskAPI #PostgreSQL #Docker #DataPipeline #TMDB #MetMovieAPI #GitHub #Contribute #Collaborate #Innovate

      Feel free to engage with the project, share your thoughts, and join me in this journey of continuous learning and growth! 🚀🔍
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Name: AI Integrated Projects
      
      Purpose: To explore AI integration for real-time detection and positioning tasks.
      
      Details: Created innovative projects using ReactJS, React Webcam, and TensorflowJS for detecting faces, hands, gestures, objects, and body poses. Provided clear documentation and hosted the project on GitHub Pages, inviting contributors to enhance the project.
      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      I did something extraordinary this year! 🚀✨ I built some innovative real-time AI integrated projects using ReactJS, React Webcam, and TensorflowJS models. 🤖🔍 These projects focus on seamless face, hand, gesture, object and body pose detection and positioning, pushing the boundaries of AI integration. 💡💪

      In order to make it accessible and user-friendly, I made sure to provide clear documentation for the project. 📚👩‍💻 And guess what? You can even experience it live on the web using GitHub Pages! Links are present in the respective GitHub repositories🌐🔗 

      But here's where it gets even better. I'm inviting contributors to run the hosted webpage and add their tested results to the documentation. 📝🔬 Together, we can make this project even more powerful and accurate. 🤝💡

      Are you ready to join me on this exciting journey? 🌟🚀 Let's collaborate and make a significant impact in the world of AI and technology. 🌍💻

      Check it out here: https://lnkd.in/gGvQpdub
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    ),
    ChatMessage(
      content="""
      Name: Met-Social-Media-API
      
      Purpose: To develop a real-time API for social media management.
      
      Details: Built with NodeJS, PostgreSQL, and Prisma ORM, the API provides endpoints for managing social media data. Includes comprehensive documentation, a predefined Postman collection, and invites contributors to improve the project via a guided code review process.

      """, role=ChatRole.USER, name="Metta"
    ),
    ChatMessage(
      content="""
      I'm thrilled to announce the completion of a project that I've been working on called Met-Social-Media-API! 🎉🚀 It's an API server for a real-time Social Media Handler project built using NodeJS, PostgreSQL, and Prisma ORM. If you're interested, you can check it out here: https://lnkd.in/gGvQpdub

      This project comes with clear documentation and a predefined Postman collection, making it incredibly easy to understand and use. 💻📚 We've put a lot of effort into making it user-friendly and accessible to developers of all levels.

      Now, here's the exciting part: we're opening this project up for contributions! 🙌🎈 We encourage everyone to get involved and contribute to our project. If you're interested, please take a moment to read our contributing guide for more information. Your contributions will be reviewed, and after the code review process, your changes will be merged into the main codebase. We appreciate your efforts and can't wait to see your work! 👏💪

      Our API provides several endpoints for managing social media data. If you want to dive deeper into the details of these endpoints, you can refer to our comprehensive API documentation. But wait, there's more! We have made all the endpoints available in our Postman public workspace, making it even easier for you to explore and test them. 📝📊 Feel free to experiment and see what you can create!

      Join us on this exciting journey and let's make social media management a breeze! 💪

      #MetSocialMediaAPI #NodeJS #PostgreSQL #PrismaORM #API #SocialMediaManagement #postman
      """, role=ChatRole.ASSISTANT, name="Linkedin Writeup Assistant"
    )
  ]
}

def get_linkedin_chat_history(history_type:str) -> List[ChatMessage]:
  data=[
    ChatMessage(
        content="""You are 'Writeup Agent' a Linkedin post content generator. 
        Create linkedin post with the user given details.""",
        role=ChatRole.SYSTEM,
        name="Writeup-Agent"
      )
    ] 
  
  # print(data)
  return data + linkedin_chat_history[history_type]

def update_chat_history(history_type:str, data:str):
  chat_history[history_type].append(ChatMessage(content=data, role=ChatRole.USER, name="Metta"))