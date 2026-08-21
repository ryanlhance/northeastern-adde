#!/usr/bin/env python3
"""Generates data.json for the Northeastern Assistant Director fit-map page.
Single source of truth: edit this, run `python3 build_data.py`, and data.json
is rewritten. (Or just edit data.json directly, this is a convenience.)
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- Evidence (title + text shown to the reader) ----
evidence = {
  "ev-13yrs": {"title": "13 Years of Client-Facing Delivery", "text": "My career began with 6 years leading client work in film and TV + advertising and music videos. Since then, 7 years of client implementation, consulting, and stakeholder management across startups, nationwide franchises, Delta Air Lines, and Bayer."},
  "ev-service-design": {"title": "7+ Years of Service Design", "text": "7+ years as a practicing service designer with an advanced degree in the specialty, but 13+ years designing how people move through complex products, services, and operations — including service design, innovation, and design strategy roles across multiple startups and Fortune 500 corporations; Delta Air Lines and Bayer."},
  "ev-ma": {"title": "Business Innovation M.A.", "text": "M.A. in Business Innovation from SCAD's De Sole School of Business Innovation — essentially an MBA crossbred with service design, built for intrapreneurship and using design thinking to influence decision making. My B.F.A. is from SCAD as well; business for film and television."},
  "ev-credentials": {"title": "Additional Credentials & Training", "text": "Beyond my Business Innovation M.A. and my B.F.A. in entertainment business from SCAD, I am a Gallup Certified Strengths Coach. Additionally, I have a certificate in Design for Urban Mobility from the University of Amsterdam, and have done multiple innovative business trainings in niche and offer design via Traffic & Funnels and offers, leads, and business models via Acquisition.com and their events."},
  "ev-wide-industry": {"title": "Wide Industry Experience", "years": "14+ years experience", "text": "Experience across 10+ industries and hundreds of niche personas across unrelated service verticals — film and TV, agriculture, counseling, fitness, hospitality, education, logistics, sports entertainment. I learn fast, dive deep, and have a proven ability to onboard quickly to and lead in any business domain."},

  "ev-blueprinting": {"title": "Service Blueprinting", "years": "7+ years experience", "text": "Built service blueprints at every scale from a 450-point blueprint for a startup's information architecture and executive decision making to a 20,000+ point global, enterprise level blueprint to identify service, product, technology, and operational gaps and opportunities at Bayer.", "link": "https://www.hance.work/Local-Enterprise-Level-Service-Blueprint-74f9ecfa9f4a4873be1b909a7f5e37d8?pvs=25"},
  "ev-knowledge-arch-rows": {"title": "Knowledge Architecture Rows", "years": "3+ years experience", "text": "In designing for complexity with LLMs and RAG, service blueprints need a row most practitioners are not defining: knowledge architecture. For every interaction point where AI shows up, what knowledge needs to be accessible to it, and where does that knowledge come from? I add that layer to blueprints so the AI can show up as close to human as the customer needs it to in a journey, building trust instead of degrading it."},
  "ev-present-future": {"title": "Present State vs Future State", "years": "10+ years experience", "text": "I map the present state of an organization, business unit, or stakeholder journey to design the future state. The global blueprinting effort at Bayer existed to identify the present state of our tech stack and operational interactions and then make recommendations for future state: we delivered a present state map and a future state map. I did the same at Dryland Revival, mapping our current processes and then identifying new product and service opportunities for our customers and better ways of working for our teams."},
  "ev-journey-mapping": {"title": "Journey Mapping", "years": "7+ years experience", "text": "I have mapped journeys across startups, national franchises, and the Fortune 500. At Bayer I facilitated a global journey mapping effort spanning North America, Europe, and Asia-Pacific, 2,250 journey points across 27 teams, that cut environmental toxin risk 70% and raised workplace safety 30% within two quarters. At Dryland, the customer and employee journeys inside our 450 point blueprint became the source for our playbooks, org design, and project management system. I led the migration of Bayer's global, enterprise level blueprint from Miro to TheyDo so the journeys could be managed more accurately and dynamically.", "link": "https://www.hance.work/Global-Journey-Mapping-Effort-228e643935ea43aab50ee95d8f56305f?pvs=25"},
  "ev-journey-ai": {"title": "Journey Mapping with AI", "years": "3+ years experience", "text": "Service designers need to be able to build tool agnostic markdown systems and be able to articulate journeys instead of just map them. Interconnected files in this context allow a tool like Claude to traverse information rapidly and create journey maps and service blueprints as dynamic or focused as necessary for the intention of the stakeholders. In this way, a map becomes an output of the content rather than the only place the content lives. My strategy is to use each interaction point as one file, tagged with the personas, playbooks, technology, and other contexts it connects to, linking forward to the next decision points and back to the ones that lead there. Markdown outlives any single vendor, so the journey survives any migration and a visual map can be generated on demand."},
  "ev-regulatory": {"title": "Regulatory & Compliance", "years": "10+ years experience", "text": "Regulatory and compliance ownership started on film sets as an Assistant Director, where I was in charge of safety and compliance on set, responsible for cast, crew, and vendors across 40 productions. At the enterprise level, I built a layered journey map across 27 teams on Bayer's operations platform for a confidential regulatory compliance effort. I currently work with highly regulated industries like counseling."},
  "ev-systems-mapping": {"title": "Systems Mapping", "years": "13+ years experience", "text": "I build maps that help teams see the bigger picture and communicate and make decisions more efficiently. At Dryland Revival, I built a map with 100+ interaction points across all five departments. I have built comparative org charts that let a nationwide franchise see its restructure clearly enough to reorganize without a single layoff, current and future state organizational maps for entire Fortune 500 divisions, and the visual maps of crew, cast, and equipment that ran thousands of production days across six years in the film industry."},
  "ev-info-arch": {"title": "Information Architecture", "years": "10+ years experience", "text": "I structure information so people, teams, and technology can equally increase efficiency with it. I have been designing the automations and information architecture of project management systems since working in the film industry, and recently developed enterprise-wide IA for PM systems at Dryland Revival. At Bayer, I designed the information architecture of the agentic persona service, and mapped the data source architecture of the global, enterprise level future state service blueprint and tech stack recommendations. Today I architect AI native, tool agnostic knowledge systems with project flow automations and documentation structures for both human and agent ease of retrieval."},
  "ev-systems-thinking": {"title": "Systems Thinking", "years": "13+ years experience", "text": "I live in a constant state of mapping systems in my head. It is what allowed me to excel at the rapid, leadership-level decision making of being an Assistant Director on set in the film industry and helps me see consequences of business decisions that most others don't. When I walk into a room, a team, or a company, I have the system mapped in my head immediately. The blueprints, frameworks, and playbooks I design are made to help others act with the level of empathy their stakeholders need."},
  "ev-root-cause": {"title": "Root Cause Solutioning", "years": "13+ years experience", "text": "I'll spend an entire day on a single problem, because I know that resolving the system instead of the symptom saves days, weeks, or months of work later. And not just for me, but for entire teams, divisions, or organizations as a whole."},
  "ev-prototyping": {"title": "Prototyping", "years": "13+ years experience", "text": "Build context appropriate prototypes, low to high fidelity, to make ideas testable and accessible to feedback and usability. Some examples: agentic user personas built and validated inside a Fortune 500 before commercial AI tools existed, sustainable business model prototypes for Delta, and the Fans First experiences the Savannah Bananas scaled to global fame. Not to mention the rapid prototyping of sites, tools, maps, and apps in the AI era."},
  "ev-experience-design": {"title": "Experience Design", "years": "13+ years experience", "text": "I have been designing experiences professionally for over a decade. At the end of six years in the entertainment industry, I helped develop and execute the prototype \"Fans First\" experience that became the standard the Savannah Bananas then scaled to global fame. Before that, I employed experience design principles to innovate on decades old traditions as Program Director of a 1,500 person summer camp, and taught those principles to the next generation of camp leaders. Since then, I designed multi-stakeholder experiences at Delta Air Lines and Campus Carriers, lead the end-to-end farmer experience at Bayer across marketing, product, and portal surfaces, and employee and customer experiences at Bayer, Dryland Revival, and the national franchises I work with at AGS."},
  "ev-product-leadership": {"title": "End-to-End Product Leadership", "years": "7+ years experience", "text": "UX Lead on Bayer's end-to-end customer site rebuild, acting as the design side Product Manager — from the public marketing pages through the post log in customer portal — driving a 35% increase in product and service opportunities and leading user acceptance testing across the North American user base."},
  "ev-design-standards": {"title": "Design Standards", "years": "4+ years experience", "text": "Authored Bayer's Universal Design Principles, adopted across every platform under the Head of Design for the $27B Crop Sciences division."},
  "ev-architect-operator": {"title": "Architect and Operator", "years": "13+ years experience", "text": "Because my background is in operations and my expertise is in designing, I develop strategic roadmaps that don't die in the purgatory between planning and executing. Before becoming a designer by training, I ran ops for a 1,500-person summer camp, a university logistics startup — a 20-truck fleet, a 100,000-square-foot warehouse, 200+ seasonal staff, and hundreds of projects in the entertainment industry."},
  "ev-design-fluency": {"title": "Design Fluency", "years": "7+ years experience", "text": "I'm a trained service designer with a background in operations and leading teams. My fluency in design work allows me to ask the right questions and spot risk early, because I've built the blueprints, run the research, and facilitated the workshops myself."},

  "ev-research": {"title": "Research & Discovery", "years": "7+ years experience", "text": "Discovery is where I start every engagement and conversation. Masters level training + 7 years of real world experience in ethnographic field research, stakeholder interviews, contextual inquiry, and journey mapping to turn workforce challenges into actionable solutions."},
  "ev-insights": {"title": "Prioritization via Insights", "years": "13+ years experience", "text": "As a strategist, I prioritize actions and roadmaps via active analysis. This is a muscle that has been being trained since running film sets and having to make significant, long term decisions live in the moment. I was then given the tools and additional frameworks in grad school where my research and prioritization skillsets were trained intentionally. At Bayer, ethnographic user discovery overturned product decisions external consultancies had built from business stakeholder input alone. At Delta, passing our concepts through a business model canvas reset the entire direction of the engagement. At Dryland, interviews with team leads redirected employee retention efforts, and now I guide executive teams in efforts that affect their entire company."},
  "ev-testing": {"title": "Testing & Validation", "years": "7+ years experience", "text": "Led User Acceptance Testing across a Fortune 500's North American user base, built agentic personas validated above 80% by 20+ year subject matter experts that cut UAT failures, and always run usability and prototype testing to pressure test ideas before they ship.", "link": "https://www.hance.work/User-Testing-Strategic-Recommendations-9f073d6ea0bb4bd1bef08d176895dd10?pvs=25"},
  "ev-vendor-selection": {"title": "Vendor Selection", "years": "13+ years experience", "text": "Drove the research and strategy that anchored Bayer's selection of its enterprise Customer Data Platform vendor, then structured the governance team that integrated it, translating between what the business needed, what the technology could do, and what the users would actually adopt. I have been selecting technologies and vendor partners since my film days, that could look like researching, building relationships with, and engaging 10+ external vendor partnerships on a single branded film. At Dryland, I selected our project management platform, built it end to end in ClickUp, then deliberately re-selected and rebuilt in Monday.com because the mobile experience served our field crews better. I regularly self train on unfamiliar enterprise software to the depth of evaluating vendor fit, and I evaluate against the workflows and journeys of all of the stakeholders, who will interact with the tool from different directions."},
  "ev-metrics": {"title": "Metrics Design", "years": "7+ years experience", "text": "Masters level training in metric determination: designing the right success metrics for the situation, then measuring against them. Fluent in OKRs, KPIs, NPS, adoption rate, time to launch, and satisfaction. Decision criteria that anchored client adoption logic in my work with Delta, the Franchise Criteria Canvas and priority matrices that gave a nationwide franchise an agreed standard for franchisee decisions, the SME validation threshold that gated Bayer's agentic personas before teams were allowed to rely on them, and the performance analytics, trackers, and dashboards Dryland ran on. Regularly measuring outcomes against the vision that was set: a 35% lift in product and service opportunities, a 30% rise in workplace safety, and 2% to 26% platform adoption in two months."},

  "ev-decision-frameworks": {"title": "Decision Frameworks", "years": "13+ years experience", "text": "I am a strategic framework and decision model library, and I use these tools to help teams uncover information, connect dots, and communicate clearly. If I don't have a tool perfect for helping a team make a decision, I design one in the moment. I've been building these tools myself and using them with teams professionally since working in the film industry, so I have a backlog of hundreds of models and frameworks going back 10+ years, not to mention the hundreds that I have collected from other great thought leaders."},
  "ev-business-design-thinking": {"title": "Business is a Design Thinking Problem", "years": "7+ years experience", "text": "As a design strategist, I have discovered most problems are solved with changes to business models, not tools. Typically, business processes, organizational structures, and employee experience are where design thinking makes the biggest impact in unblocking organizations, though most organizations point their design teams towards digital problems. Clients come to me asking for the right software, system, or UI/UX work, yet when I conduct research, those are rarely the bottleneck. I apply design thinking to the business itself, and have learned to influence stakeholders and C-Suite leaders outside of IT infrastructure."},
  "ev-strategic-advising": {"title": "Strategic Advising", "years": "13+ years experience", "text": "My strategic advising goes back to film and TV, where the producer's first job is advising the client on their own vision: what is actually possible within the timeline and budget, and what it will take to get there. Since then: primary client contact for Delta Air Lines leading a sustainability marketing effort, almost eight years of coaching leaders through my own practices, and advising for franchisees and franchisors today."},
  "ev-process-optimization": {"title": "Process Optimization", "years": "13+ years experience", "text": "My background in film means that the first half of my career required doing literally unbelievable things with scarce resources. Now, I reengineer systems to allow for the streamlining of resources that will exercise the greatest efficiency. I helped a university logistics operation restructure for a 60% resource reduction, built a startup playbook library that lifted efficiency 80% and removed the CEO from lower-level decisions, and developed operating cadences and management systems that kept teams aligned through rapid growth in both my entertainment industry days and my startup experiences."},

  "ev-change": {"title": "Change Management", "years": "12+ years experience", "text": "Drove change and adoption in resistant systems my entire career: from navigating day-to-day and hour-by-hour changes on film sets to innovating decades old traditions while keeping the soul of the experience at a 1,500 person summer camp, including a decade old training program replaced with modern methods, creating a 67% year over year retention lift; a nationwide counseling franchise led through restructuring across states without a single layoff; a startup org redesign that doubled revenue and quadrupled headcount; moving a construction field crew into modern technology in the context of a phone based project management system; and leading a Fortune 500 AI platform from 2% to 26% adoption in two months."},
  "ev-operating-cadences": {"title": "Operating Cadences", "years": "13+ years experience", "text": "Ran daily risk tracking and hour by hour plans across teams of 15 to 60 and multiple concurrent productions in the film industry. At Bayer, I built the scrum board, wrote the stories, and led scrum for a legacy platform team that had no ceremonies at all. At Dryland, I owned the operating cadences and reporting: the all hands meetings, trackers, and dashboards that all six teams ran on through a growth window that doubled revenue and quadrupled headcount year over year. Actively leading interaction cadences throughout my coaching programs the last eight years. Led operating cadences at Campus Carriers, Greene Family Camp, and the Delta Air Lines effort as well."},
  "ev-workforce-transformation": {"title": "Workforce Transformation", "years": "10+ years experience", "text": "Workforce transformation in four settings: Bayer's employee experience platform, end to end people operations at Dryland Revival from hiring funnel to playbooks, the nationwide restructuring of a counseling franchise, and multiple entertainment industry efforts restructuring teams after budget and timeline changes."},

  "ev-engagement-ownership": {"title": "Engagement Ownership", "years": "13+ years experience", "text": "I lead multiple concurrent client engagements end to end, owning scoping, timeline, and delivery from discovery through handoff. This skillset developed in film and TV first, where our crew averaged six productions at a time and peaked between ten and twelve. I also owned multiple engagements with business stakeholders as a design leader at Bayer and Delta Airlines."},
  "ev-e2e-client": {"title": "End-to-End Client Delivery", "years": "13+ years experience", "text": "Six years in film and TV owning productions end to end as the client's point of contact, on time and on budget across roughly 50 productions, including a branded film for Hamilton Watches spanning 30+ crew, 20+ talent, eight locations, and ten-plus vendor partners. Then Delta, where I was the primary contact between client and team, presenting at corporate while translating business needs to the creative team in the studio. Today I own consulting engagements end to end for franchisors, franchisees, and service businesses, from scoping and discovery through implementation and adoption."},
  "ev-high-stakes-decisions": {"title": "High Stakes Decision Making", "years": "13+ years experience", "text": "As an assistant director and production coordinator in the entertainment industry, my brain was the on-set hub for information, prioritization, and decision-making across 40 productions, coordinating thousands of crew, cast, and vendors live — and de-escalating the \"whatever can go wrong will go wrong\" situations."},
  "ev-rapid-domain": {"title": "Rapid Domain Learning", "years": "13+ years experience", "text": "Joined into a Fortune 500 knowing nothing about agriculture and was shipping across four platforms within a year. Joined Dryland knowing nothing about construction sciences and grew the business to profitability within two years. Have done relevant and successful consulting work in 10+ unfamiliar domains."},
  "ev-agile": {"title": "Agile Experience", "years": "4+ years experience", "text": "Worked inside agile product teams across four Bayer platforms: refined backlogs, aligned hundreds of technical stories to user needs, led user acceptance testing across the North American user base, then built out the scrum board — writing all the stories and leading scrum — for a legacy platform team."},

  "ev-mentorship": {"title": "Mentorship Experience", "years": "12+ years experience", "text": "Ran training and development for a 250 person camp staff, redesigning a program that lifted retention 67% year over year, am Gallup certified, trained leadership coach with almost eight years running my own coaching practice, and spent six years in film identifying underutilized talent, developing them through on set mentor matching, and enabling them to lead their own crews."},
  "ev-training-program": {"title": "Training Program Design", "years": "7+ years experience", "text": "Redesigned a decade old staff training program at one of the country's largest residential summer camps (1,500 people a summer) using Self-Determination Theory as the leadership framework — driving a 67% year-over-year staff retention increase. This was after developing leadership training for the internal and external stakeholders at Campus Carriers and developing leadership programming for teens and young professionals, and before my more recent efforts designing leadership training for men 20s to 40s."},
  "ev-coaching": {"title": "Coaching", "years": "7+ years experience", "text": "Gallup Certified Strengths Coach trained in behavior and relationship psychology; almost eight years of facilitating leadership development in the context of empathy strategies and emotional intelligence professionally. Built a leadership development practice from scratch to five figure revenue months within six months, running and iterating workshops and facilitation opportunities since. I've coached hundreds of high school and college students through multi-month social-emotional learning and leadership programs, and hundreds of others through weekend retreats, cohorts, and high ticket 1:1 men's work, with custom tools for mental and emotional processing developed in line with my systems and design thinking background."},
  "ev-psych": {"title": "Human Behavior & Psychology", "years": "12+ years experience", "text": "Gallup Certified Strengths Coach trained in behavior and relationship psychology. This guides my deep empathy for user behavior, and my ability to influence change without authority. Eight years of teaching emotional intelligence and social emotional learning professionally means I can read motivations, needs and expectations, and emotions as a professional expertise, not a personality trait. I use that background to shape desirability and adoption."},

  "ev-xfn": {"title": "Cross-Functional Leadership", "years": "13+ years experience", "text": "I have led across functions and disciplines my entire career. On film sets, every department head came to me as the hub for information, prioritization, and decision making across thousands of crew, cast, and vendors. At Delta, I led a cross-cultural team spanning eight countries and nine disciplines while owning budget, timelines, and the client relationship, presenting at corporate and translating business needs to the creative team in the studio. At Bayer, I aligned 27 teams that did not report to me across North America, Europe, and Asia-Pacific. At Dryland, all six teams ran on the operating systems I developed."},
  "ev-translator": {"title": "Cross Discipline Fluency", "years": "13+ years experience", "text": "Fluent in business, design, and engineering languages. I love translating business jargon to design requirements, engineering capabilities to business possibilities, and design visions to engineering roadmaps. This is the product and service version of what I did as a producer and assistant director in the entertainment industry in the first half of my career."},
  "ev-facilitation": {"title": "Workshop Facilitation", "years": "12+ years experience", "text": "I have practiced facilitation professionally for over a decade. Hundreds of design thinking workshops from 5 to 150 people at Bayer, where Miro selected me as the sole Enterprise Advocate for a company of ~100,000 people. Staff trainings, development programming, and multi-day events for a 250 person staff at one of the country's largest summer camps. Eight years of leadership retreats, cohorts, and group trainings through my own practices, from high school and college students to the men's work I facilitate today. And the working sessions I currently run with franchise corporate teams and franchisees."},
  "ev-speaking": {"title": "Public Speaking & Presentations", "years": "10+ years experience", "text": "Over a decade of live presentations, from pitch decks in Fortune 500 corporate rooms to multi-day retreats, scaled coaching programs, and live events for a 1,500-person camp. Comfortable commanding a room of five people to five thousand."},
  "ev-exec-alignment": {"title": "Executive Alignment", "years": "10+ years experience", "text": "At Bayer, I developed an agentic AI experience and sold it internally through months of workshops, demos, and one on one influencing before getting the greenlight to build. At Delta, I was the primary client contact, presenting status updates and pitch decks regularly to corporate. As a franchise consultant, I work directly with CEOs, executive teams, and franchisors. At Dryland, I was the CEO's first conversation and advisor on every major decision. The first half of my career in film was aligning clients and directors on what was actually possible within the timeline and budget."},
  "ev-storytelling": {"title": "Storytelling & Executive Narrative", "years": "10+ years experience", "text": "Ten years writing 20 to 50 pages a week of creative and business content, from user stories to executive strategy. As Delta's primary client contact I presented status updates and pitch decks in corporate rooms while translating business needs to the creative team, and I sold an agentic AI build to Bayer executives through months of workshops, demos, and one-on-one narrative."},
  "ev-strategic-writing": {"title": "Strategic Writing & Documentation", "years": "10+ years experience", "text": "Built upon a practice of writing 20 to 50 pages a week, I have delivered hundreds of scripts and character driven narratives, as well as hundreds of pages of strategic documentation, philosophical essays, user stories, and executive strategy. I authored Bayer's Universal Design Principles, adopted across every platform in the division, the Customer Data Platform strategy documentation that anchored vendor selection at the enterprise level, and the AI Strategy Playbook shipped in 20+ languages. Today I write the documentation depth that powers tool agnostic AI knowledge management."},
  "ev-curriculum": {"title": "Curriculum & Learning Design", "years": "7+ years experience", "text": "Designed learning programs and curricula end to end: a leadership curriculum across seven partner universities, multi-month social emotional learning and leadership programs and retreat curricula for high school and college students, high ticket 1:1 men's work including course material, custom processing tools, and interaction cadences, the cohort and retreat programming I still run for men in their 20s, 30s, and 40s, a redesigned staff training program at a 1,500 person camp that lifted retention 67% year over year, and AI enablement content, guides, and quick reference materials for thousands of Fortune 500 users."},
  "ev-global": {"title": "Global & Cross-Cultural Work", "years": "7+ years experience", "text": "Led a team at Delta spanning eight countries and nine disciplines, a global journey mapping effort across North America, Europe, and Asia-Pacific, and AI enablement at Bayer delivered in 20+ languages from Indonesia to Brazil."},

  "ev-adoption": {"title": "Tool and AI Adoption", "years": "10+ years experience", "text": "Adoption is a design problem. At Bayer, I took a Fortune 500's internal AI platform from 2% to 26% adoption in two months, by treating it as a competence problem rather than a trust problem. Beyond that, I developed an agentic persona service that multiple anti-AI teams started using daily, a project management system that construction field crews actually used on their phones, the migration of Bayer's global blueprint from Miro to TheyDo that matured design thinking across the enterprise through ease of discovery for customer journey maps, and currently lead teams from Notion, Dropbox, and Google Drive into tool agnostic markdown systems that increases their AI usage. This passion started in the film industry where I led the adoption of on-set and pre-production technologies across teams and departments."},
  "ev-ai-training": {"title": "Global AI Training", "years": "3+ years experience", "text": "Authored Bayer's AI Strategy Playbook and led its global dissemination in 20+ languages to thousands of internal users across business, engineering, design, and HR — training entire departments of the business from Indonesia to Brazil in a single quarter.", "link": "https://www.hance.work/Generative-A-I-Playbook-bb68ca8c80d840e5be083136a0b88f92?pvs=25"},
  "ev-ai-agents": {"title": "Building AI Agents", "years": "3+ years experience", "text": "Pioneered an agentic persona service at Bayer in 2023, before commercial agents were available. I built AI models of users our design team couldn't otherwise reach, wired into Microsoft Teams before commercial AI integrations existed for the company's stack. The workflow produced high fidelity user representations rapidly, validated by SMEs above 80% accuracy, and significantly reduced UAT failures across the teams that used them. That was over 3 years ago. Imagine what I can do with your data and Claude's newest features.", "link": "https://www.hance.work/A-I-Persona-Prototypes-43575337f52c4cecaf4fdd871e5aa41e?pvs=25"},
  "ev-agentic-ops": {"title": "Agentic Operations Design", "years": "3+ years experience", "text": "Currently transforming business operations through agentic experience design alongside human and AI skill development, increasing the efficiency and accuracy of leaders, teams, and individual contributors. I own transformation engagements from scoping and discovery through implementation and adoption, and build AI-native, tool-agnostic knowledge management systems for creative and operational teams, architected for both human and agent ease of retrieval."},
  "ev-responsible-ai": {"title": "Responsible AI", "years": "3+ years experience", "text": "I've been integrating AI into human systems since before commercial integrations existed — agentic personas validated by 20+ year subject-matter experts above 80% accuracy before teams were allowed to rely on them. I've also led stakeholder AI education from Indonesia to Brazil, and designed governance gates for agents to reduce failures and overstepping."},
  "ev-ai-tool-eval": {"title": "AI Tool Evaluation", "years": "4+ years experience", "text": "Regularly self train on unfamiliar enterprise software to the depth of evaluating vendor fit, proven at the Fortune 500 level and across startups. Drove a Fortune 500's Customer Data Platform vendor selection and gave strategic input on its internal LLM platform build. My goal is to identify the right tool for the right job and the right persona."},
  "ev-knowledge-mgmt": {"title": "Knowledge Management", "years": "3+ years AI native experience", "text": "Building knowledge management systems across multiple technologies and technological eras. My priority is KM for retrieval augmented AI. I design AI-native, tool-agnostic hubs and agentic decision-making systems architected for both human and agent ease of retrieval. I believe the next few years of tech growth will see knowledge management and access as the top priority. I have been developing AI enabled experiences on that assumption since 2023 at the Fortune 500 level."},
  "ev-ai-retrieval": {"title": "Designing for AI Retrieval", "years": "3+ years experience", "text": "In a post-LLM integrated world, design strategists need to be able to design the information architecture and retrieval directories that help LLMs find the right information and make decisions inside large knowledge bases. There are two types of decisions to design for: retrieval decisions and content decisions. Retrieval decisions are how the system finds something, and content decisions are what gets searched for and pulled for outputs. I build retrieval guides and decision-making architecture into the knowledge system I design for clients."},
  "ev-ai-product": {"title": "AI Product Strategy", "years": "3+ years experience", "text": "Led product strategy on the build out and adoption of Bayer's internal LLM platform pre-AI-boom, impacting design and product decisions and leading user testing. I partnered in developing the platform's use cases with its beta users, with one of those use cases later measuring 23.3% average time saved and 10.7 working days saved per worker per year in the relevant area in a peer-reviewed external study. That work continues today as the core of my consulting practice. I build agentic, tool agnostic knowledge systems for creative and operational teams, design the prompt, workflow, and rule configurations they run on, and treat retrieval quality and human authored context as the leverage priority.", "link": "https://www.hance.work/A-I-Product-Roadmap-d042f4d986e5441bbb80b5e5ea4bd018?pvs=25"},
  "ev-ai-reliability": {"title": "AI Reliability & Quality", "years": "3+ years experience", "text": "Build AI systems that perform reliably in production by treating the knowledge layer as the priority. SME written or validated content over endless prompt tuning, corpus audits for the percentage actually authored by humans, retrieval and validation management and measurement, and active guarding against the context dilution that comes from LLMs overwriting good context over time. Proven at the Fortune 500 level at Bayer, where agentic personas grounded on internal research and customer data were validated above 80% accuracy by subject matter experts with 20+ years in the field."},
  "ev-rd-lab": {"title": "Personal R&D Lab", "years": "16+ years experience", "text": "My personal life is a constantly running R&D lab — I've been ramping on a new technology at least once a quarter since high school, and my current operating system pairs agentic AI workflows with a digital brain to extend what I can do. I love unfamiliar domains and emerging tech."},

  "ev-playbook": {"title": "Playbook Writing", "years": "10+ years experience", "text": "Built an operations playbook at Campus Carriers that cut resource needs 60%, an entire startup playbook library that lifted efficiency 80% and removed the CEO from lower-level decisions at Dryland Revival, and a Fortune 500 AI strategy playbook shipped in 20+ languages at Bayer. This was all built on the foundation of playbook building for my teams in the film industry."},
  "ev-pm-system": {"title": "PM System Design", "years": "10+ years experience", "text": "I have designed and facilitated project management systems my whole career. In film, I designed the project management system that managed hundreds of productions and kept projects on time and on budget while our crew averaged six productions at a time, peaking between ten and twelve. At Dryland, I designed the automations and information architecture end to end: built in ClickUp, rebuilt in Monday.com and run on Zapier automations. Prioritizing one click steps for every stakeholder in each process. At Bayer, I built out the scrum board and wrote all the stories for a legacy platform team that had no user stories or change tracking. Today I build project management systems in Notion and Claude for clients and my own operation."},
  "ev-pm-tools": {"title": "PM Tool Fluency", "years": "13+ years experience", "text": "I've built project management systems end-to-end in ClickUp, Monday.com, Notion, Aha!, Motion, and Claude, and regularly self train on unfamiliar enterprise software to the depth of being able to evaluate vendor fit. Proven experience across startups, the entertainment industry, and the Fortune 500 level."},
  "ev-tooling": {"title": "Tooling & Platforms", "years": "16+ years experience", "text": "Fluent across the tech stack I have built and shipped projects in: design and mapping (Miro, Mural, TheyDo), knowledge and docs (Notion, Obsidian), project management (Monday.com, ClickUp, Asana, Jira, Aha!, Motion, Profit.co), AI (Claude Code, Claude Cowork, the Claude API, ChatGPT and the OpenAI API, agentic tooling), research and analytics (MAXQDA, DisplayR, QuestionPro), commerce (Shopify), and the everyday collaboration tools (Microsoft 365, Google Suite, Slack, Zoom, Loom, Dropbox). I self train on unfamiliar enterprise software to the depth of evaluating vendor fit at least once a quarter."},
  "ev-tool-migration": {"title": "Enterprise Tool Migration", "years": "4+ years experience", "text": "Led the migration of Bayer's global, enterprise level service blueprint from Miro to TheyDo — customer journey enablement at the enterprise level. I have also led multiple teams in migrating from Notion, Dropbox, Google Drive, and other knowledge sources to Obsidian via markdown strategy to become tool agnostic super users of their own information."},

  "ev-roadmapping": {"title": "Product Management & Roadmapping", "years": "13+ years experience", "text": "Being a producer in the film industry was a 1:1 mirror of product management: understand the client's vision, close the gap between what they think is possible and what the timeline and budget allow, build the roadmap, own delivery, develop and lead teams. Running six concurrent productions on average mirrors running parallel product lines, each with its own stakeholders, budget, and hard ship date. After a masters degree that specifically focused on the intersection of business and design, I carried that operating model into Fortune 500 environments, leading product and project management for a sixteen person, eight country, nine discipline team developing sustainable business models for Delta Air Lines. Then at Bayer: acting as the design-side Product Manager for the end-to-end farmer experience, leading strategic input and user testing on Bayer's internal LLM platform build, determining the platform-wide integration roadmap of the Customer Data Platform, the internal AI product roadmap, plus backlog refinement, user story writing, and building out an agile scrum board for a legacy platform team that had none."},
  "ev-gtm": {"title": "Go-to-Market & Offer Design", "years": "7+ years experience", "text": "Structured the offer and go-to-market strategy for seven intrapreneurial and entrepreneurial ventures: an internal agentic tool at Bayer, sustainable products at Delta Air Lines, an education as a service line with Campus Carriers, the business model for Dryland Revival, multiple successful leadership practices, my franchise consulting business. Formal training in business modeling and GTM strategy (M.A. program at SCAD), niche and offer design (Traffic & Funnels) and offers, leads, and business models (Acquisition.com). I take an opportunity from value proposition to packaging, and into a working product or service."},
  "ev-biz-model": {"title": "Business Model Design", "years": "7+ years experience", "text": "Designed business models, tech stacks, and service models across many engagements: agentic tools within Bayer, sustainable business models for Delta's obsolete beverage carts, a construction-science startup's operating model, a B2B2C education as a service for Campus Carriers, a hospitality franchise's multi-location tech roadmap, and five personal ventures grown to profitability."},
  "ev-new-revenue": {"title": "New Revenue Lines", "years": "13+ years experience", "text": "I have pioneered new revenue lines across startups, franchises, and the Fortune 500. Developed a B2B2C education as a service line at Campus Carriers, owned end to end from primary market research through curriculum design, offer design, and pre-launch partnerships across seven partner universities. New service offerings designed and launched at Dryland Revival through a growth run that doubled revenue year over year for three years. Sustainable business models for thousands of Delta's obsolete beverage carts. An operations and marketing transformation at a physical health franchisee that opened the path to a second location. And my own ventures: a bicycle rental marketplace for a university, a community based product business grown to profitability, a vending machine business grown to profitability and exited, and multiple coaching and consulting practices grown to recurring five figure months."},
  "ev-org-restructuring": {"title": "Organizational Restructuring", "years": "9+ years experience", "text": "I have restructured organizations in three settings. A nationwide counseling franchise across multiple states: ethnographic interviews with corporate and franchisees, comparative org charts, and a Franchise Criteria Canvas that gave corporate a clear standard, with locations closed, folded, and opened and headquarters reorganized without a single layoff. Dryland Revival: an org redesign that detached the CEO from daily hands on work, doubling revenue and quadrupling headcount in three months. Campus Carriers: reformed the organizational structure and operational systems of the university logistics operation for a 60% resource reduction."},
  "ev-talent-dev": {"title": "Talent Development", "years": "10+ years experience", "text": "Built individualized development plans across a 250 person camp staff, created a system for on set mentor matching in film that identified underused talent and launched them to lead their own crews, and design and facilitate leadership programming for the last eight years."},
  "ev-team-retention": {"title": "Team Retention", "years": "10+ years experience", "text": "I build teams that stick around. Some stats: roughly 95% crew retention across six years in film, a 67% year-over-year retention lift at a 250 staff summer camp, and a startup hiring funnel that delivered 100% season-long retention of the individuals who moved through it."},
  "ev-hiring": {"title": "Hiring Experience", "years": "13+ years experience", "text": "I have built and run hiring systems in three industries. In film and TV, I built and led a multi-departmental production crew with roughly 95% project to project retention across six years, identifying underutilized talent and developing them into leads through on set mentor matching. At Campus Carriers, I facilitated the seasonal staffing funnel, hiring and training 50 to 100 employees a year. At Dryland, I built the hiring funnel across three candidate markets that scaled the team from 3 to 15 in a single season and 30 to 40 hires across seasons, conducting hundreds of first round interviews and designing a paid multi-day field test that drove 100% season long retention of everyone who completed it."},
  "ev-startup-os": {"title": "Startup Operating Systems", "years": "9+ years experience", "text": "I have built the operating systems of two startups. At Campus Carriers, a university logistics startup, I ran the largest location \u2014 a 20 truck fleet, a 100,000 square foot warehouse, and 200+ seasonal staff. I built the operational playbook covering recruiting, onboarding, training, scheduling, inventory, and safety that drove a 60% resource reduction and propagated across the other partner campuses, while pioneering an education as a service revenue line on top of it. At Dryland Revival, as co-founder and second hire, I built the operating system as we grew from one client to a profitable exit: playbooks, hiring funnel, project management system and tech stack, and the org redesign that let the CEO focus on his highest leverage work."},
  "ev-resource-reduction": {"title": "Resource Reduction", "years": "10+ years experience", "text": "Leading film industry efforts required creative prioritization to arrive at the final vision on time and on budget. Another example is the reformation of the operational systems and org structure at a university logistics startup \u2014 a 100,000 square foot warehouse, a 20-truck fleet, and 200+ seasonal staff \u2014 where I then documented the new ways of working into the playbook that propagated across all campuses. The reform drove a 60% resource reduction. This was all pre-service design and business modeling expertise, the framework I have used to make and communicate these decisions across my Fortune 500 and consulting work since."},
  "ev-concurrent-pm": {"title": "Concurrent Project Management", "years": "10+ years experience", "text": "Owned film and TV productions end to end as the client's point of contact, delivering on time and on budget while running an average of six concurrent productions, peaking at ten to twelve multiple times. Currently managing multiple engagements with AGS."},
  "ev-workstreams": {"title": "Multiple Workstreams", "years": "13+ years experience", "text": "Like my time in the entertainment industry, summer camping, and consulting, my role at Bayer was constantly in flux. I started as the UX lead for the farmer experience, became a design strategist for the operations platforms, then lead strategist for the generative AI effort, turning a six month contract into 18 months by continuing to be useful. I ramp quickly on new problems."},
  "ev-parallel": {"title": "Parallel Workloads", "years": "13+ years experience", "text": "Built a startup to a profitable exit while working Bayer full time \u2014 Bayer was my 9-to-5, the startup was my 5-to-9. Two demanding roles, years of switching between them without dropping the ball. Before this, 6+ years running multiple projects at a time in the entertainment and summer camping industries in parallel. My capacity for effort is high."},
  "ev-tech-stack": {"title": "Tech Stack Blueprinting", "years": "7+ years experience", "text": "Bayer's global enterprise blueprinting effort was tech stack blueprinting at the largest possible scale: mapping the present state of every tech stack, persona, and operational interaction across multiple countries, then delivering future state recommendations that exposed redundant systems and unserved gaps. At Dryland, the 450 point blueprint drove the design and redesign of our entire tech stack, from the original ClickUp buildout to a Monday.com rebuild and the Zapier automations connecting it all. I still do this for clients today, including the end-to-end service blueprint and strategic recommendations that determined a hospitality franchise's tech stack roadmap for multi-location build outs."},
  "pf-cdp": {"title": "Customer Data Platform Roadmap", "text": "The use cases and roadmap, built from the customer-experience perspective, that anchored a Fortune 500's Customer Data Platform vendor selection.", "link": "https://www.hance.work/Customer-Data-Platform-Roadmap-0d65a3c99943497e9c969160e33742a2?pvs=25"},
  "pf-personas": {"title": "A.I. Persona Prototypes", "text": "Agentic AI personas wired into Microsoft Teams \u2014 built before commercial AI integrations existed and launched across multiple company-wide platforms \u2014 so teams could interview user models they couldn't otherwise reach.", "link": "https://www.hance.work/A-I-Persona-Prototypes-43575337f52c4cecaf4fdd871e5aa41e?pvs=25"},
  "ev-high-stakes-env": {"title": "High Stakes Environments", "years": "13+ years experience", "text": "As a producer and assistant director in the entertainment industry, plans had to be precise, teams had to be well-qualified, and the roadmap had to be intentional. If we had to push a day, we might be literally wasting a million dollars, and that responsibility fell directly on me. This was normal as a work environment for me for six years."},
  "ev-constraints": {"title": "Working Within Constraints", "years": "13+ years experience", "text": "As a producer and assistant director, my whole job was making the client and directors' visions possible despite budget, time, and resource constraints \u2014 I developed the concept and vision, roadmapped, and implemented the operational plan across years of productions. This has translated directly to my skillsets in producing quality work creatively since."},
  "ev-early-risk": {"title": "Early Risk Flagging", "years": "13+ years experience", "text": "Skilled at identifying delivery risk early in unfamiliar domains \u2014 a habit built through six years of film sets where the surprises required quick production-wide changes, seven years in summer camping where one lightning strike could change the plans for 500 kids for a whole day, and running operations across multiple startups."},
  "ev-evaluating-inherited": {"title": "Evaluating Inherited Work", "years": "10+ years experience", "text": "I am regularly handed someone else's work and asked to move forward from where they left off. This was common in the film industry and most of my efforts in other operational capacities like at Campus Carriers and Greene Family Camp. At Bayer, my first assignment on the operations platform was user acceptance testing with zero context on products built before we arrived. Additionally, my first assignment with the customer platform was to take over ownership of the primary user experience for the end-to-end farmer site rebuild, where I immediately discovered a gap in designing for user trust by the external consultancies. Entering a project without the builders' context is an advantage, because most users of a product, service, or system do not have that context either."},
  "pf-full": {"title": "Full Portfolio", "text": "Twelve public case studies across service blueprints, journey maps, systems maps, AI strategy, and UX — each one walks through the process, the deliverables, and the impact.", "link": "https://www.hance.work/"},
  "pf-local-blueprint": {"title": "Local Enterprise Service Blueprint", "text": "A focused enterprise service blueprint mapping a business's systems and interaction points end to end.", "link": "https://www.hance.work/Local-Enterprise-Level-Service-Blueprint-74f9ecfa9f4a4873be1b909a7f5e37d8?pvs=25"},
  "pf-global-blueprint": {"title": "Global Enterprise Service Blueprint", "text": "Bayer's 20,000+ point global service blueprint mapping tech, personas, and interactions across countries to surface redundancies and gaps.", "link": "https://www.hance.work/Global-Enterprise-Level-Service-Blueprint-cd937db4cb344b318bae4c6d1e7ca9fa?pvs=25"},
  "pf-eraf": {"title": "Systems Flow (ERAF) Map", "text": "A systems-flow map of 100+ interaction points that helped siloed teams see their role in the larger business — and kept employees who were ready to quit over 'bad communication.'", "link": "https://www.hance.work/Systems-Flow-ERAF-Map-74cfa7e910564777a9883a55f066d4f9?pvs=25"},
  "pf-ai-roadmap": {"title": "A.I. Product Roadmap", "text": "Product roadmap for a Fortune 500's internal AI platform, defining the use cases and the path to adoption.", "link": "https://www.hance.work/A-I-Product-Roadmap-d042f4d986e5441bbb80b5e5ea4bd018?pvs=25"},
  "pf-genai-playbook": {"title": "Generative A.I. Playbook", "text": "The AI strategy playbook that drove adoption from 2% to 26%, shipped in 20+ languages to thousands of users.", "link": "https://www.hance.work/Generative-A-I-Playbook-bb68ca8c80d840e5be083136a0b88f92?pvs=25"},
  "pf-prompt-eng": {"title": "Prompt Engineering Strategic Design", "text": "A prompt engineering approach and template that let non-technical stakeholders across the company use generative AI effectively for the first time.", "link": "https://www.hance.work/Prompt-Engineering-Strategic-Design-40891c882c00477e936743a5d0657ddc?pvs=25"},
  "pf-user-testing": {"title": "User Testing Strategic Recommendations", "text": "Using user research and testing to inform strategic product development on a supply chain platform.", "link": "https://www.hance.work/User-Testing-Strategic-Recommendations-9f073d6ea0bb4bd1bef08d176895dd10?pvs=25"},
  "pf-platform-playbook": {"title": "Platform Design Playbook", "text": "A reusable playbook for designing and standing up new platforms.", "link": "https://www.hance.work/Platform-Design-Playbook-838ea8da681f4577bce28f0ea7e30b67?pvs=25"},
  "pf-legacy-ux": {"title": "Legacy Software UX Strategy", "text": "Restructured forms, progress indicators, and language to make a legacy platform more efficient and usable.", "link": "https://www.hance.work/Legacy-Software-UX-Strategy-e189dab0fccc4d088f0f8e2a22b009a9?pvs=25"},
}




def ph(pid, text, ev):
    return {"id": pid, "text": text, "evidence": ev}


def jd_prose():
    return [
      {"type": "h2", "text": "Job Summary"},

      {"type": "p", "segments": [
        "The Assistant Director of Digital Enablement ",
        ph("a-strategic-ops-leadership", "provides strategic and operational leadership across digital solutions consulting, solutions engineering, and training",
           ["ev-architect-operator", "ev-startup-os", "ev-workstreams"]),
        ", with a ",
        ph("a-ai-enablement-focus", "significant focus on AI enablement across the university",
           ["ev-ai-training", "ev-adoption", "pf-genai-playbook"]),
        ". This role intentionally ",
        ph("a-unified-model", "unifies consultation, solution design, implementation, and training into a single, integrated service model recognizing that effective consultations are inherently instructional, strong training is consultative, and successful digital solutions require both",
           ["ev-e2e-client", "ev-service-design", "ev-agentic-ops", "ev-design-fluency"]),
        ".  A primary role of this position is the ability to ",
        ph("a-senior-stakeholders", "work closely with senior stakeholders (Director, VP, etc.)",
           ["ev-exec-alignment", "ev-strategic-advising", "ev-speaking"]),
        " to ",
        ph("a-transformation-roadmaps", "create and shape AI transformation roadmaps",
           ["ev-ai-product", "ev-roadmapping", "pf-ai-roadmap"]),
        ", ",
        ph("a-evaluate-vendors", "research and evaluate vendors that can deliver on strategic AI initiatives",
           ["ev-vendor-selection", "ev-ai-tool-eval", "pf-cdp"]),
        "."
      ]},

      {"type": "p", "segments": [
        "Reporting to the Director of Digital Solutions and Global Client Experience, the Assistant Director ",
        ph("a-multidisciplinary-teams", "oversees multidisciplinary teams",
           ["ev-xfn", "ev-talent-dev", "ev-hiring"]),
        " responsible for ",
        ph("a-community-adopt", "enabling the university community to effectively adopt and use enterprise platforms, AI-powered tools, and digital workflows",
           ["ev-adoption", "ev-tool-migration", "ev-ai-training"]),
        ". This role serves as a ",
        ph("a-bridge", "bridge between campus needs and IT capabilities",
           ["ev-translator", "ev-design-fluency", "ev-systems-mapping"]),
        ", ensuring solutions are ",
        ph("a-user-centered-documented", "user-centered, scalable, well-documented, and supported by high-quality enablement experiences",
           ["ev-experience-design", "ev-strategic-writing", "ev-info-arch", "ev-curriculum"]),
        "."
      ]},

      {"type": "p", "segments": [
        "A core emphasis of this role is AI enablement: ",
        ph("a-adoption-diffusion", "guiding the adoption, diffusion, and effective use of AI platforms and AI-embedded tools (e.g., Microsoft Copilot and other emerging technologies) through solution design",
           ["ev-adoption", "ev-ai-agents", "ev-ai-tool-eval", "pf-genai-playbook"]),
        ", ",
        ph("a-process-reengineering", "process reengineering",
           ["ev-process-optimization", "ev-present-future", "ev-journey-mapping", "pf-local-blueprint", "ev-business-design-thinking"]),
        ", ",
        ph("a-consulting-training", "consulting, training",
           ["ev-e2e-client", "ev-ai-training", "ev-facilitation"]),
        ", and ",
        ph("a-change-management", "change management",
           ["ev-change", "ev-workforce-transformation"]),
        ". The Assistant Director will ",
        ph("a-oversee-ai-roles", "directly oversee senior AI-focused roles",
           ["ev-mentorship", "ev-talent-dev"]),
        " and is expected to ",
        ph("a-model-ai-fluency", "model strong AI fluency, ethical use, and practical application across administrative and academic contexts",
           ["ev-responsible-ai", "ev-agentic-ops", "ev-rd-lab", "ev-ai-reliability"]),
        "."
      ]},

      {"type": "h3", "text": "24/7 business continuity:"},

      {"type": "p", "segments": [
        "This role requires ",
        ph("a-after-hours", "occasional availability outside of traditional working hours to address urgent business needs as they arise",
           ["ev-high-stakes-env", "ev-parallel", "ev-operating-cadences"]),
        ", including, but not limited to, ",
        ph("a-incidents", "responding to security incidents, supporting software deployments, resolving software issues or system breaks, and addressing other critical operational requirements",
           ["ev-high-stakes-decisions", "ev-early-risk", "ev-root-cause"]),
        ". The ideal candidate must be ",
        ph("a-minimal-disruption", "proactive and adaptable, ensuring minimal disruption to business operations by promptly addressing any issues, regardless of time or day",
           ["ev-early-risk", "ev-high-stakes-env", "ev-concurrent-pm"]),
        ". ",
        ph("a-urgency", "Flexibility and a strong sense of urgency are essential for success in this position",
           ["ev-constraints", "ev-high-stakes-decisions"]),
        "."
      ]},

      {"type": "h3", "text": "Other duties as required:"},

      {"type": "p", "segments": [
        "This role requires ",
        ph("a-outside-primary", "flexibility in performing duties outside of the primary responsibilities to support evolving business needs",
           ["ev-workstreams", "ev-wide-industry"]),
        ". The ideal candidate must be ",
        ph("a-additional-tasks", "adaptable and willing to take on additional tasks or projects as required, ensuring smooth operations across the organization",
           ["ev-evaluating-inherited", "ev-rapid-domain"]),
        ". This may include ",
        ph("a-stepping-in", "stepping in to assist with cross-functional teams, handling unexpected challenges, or contributing to initiatives that support business growth and success",
           ["ev-xfn", "ev-early-risk", "ev-new-revenue"]),
        ". ",
        ph("a-pivot", "A proactive mindset and the ability to pivot quickly are essential for thriving in this dynamic environment",
           ["ev-rapid-domain", "ev-workstreams", "ev-constraints"]),
        "."
      ]},

      {"type": "h2", "text": "Minimum Qualifications"},

      {"type": "li", "segments": [
        ph("a-bachelors", "Bachelor’s degree in Information Technology, Computer Science, Business, Education, or a related field; or equivalent combination of education and experience",
           ["ev-ma", "ev-credentials"]),
        "."
      ]},

      {"type": "li", "segments": [
        ph("a-seven-years", "7+ years of experience in digital solutions consulting, solutions engineering, training, product/platform ownership, or digital transformation roles",
           ["ev-13yrs", "ev-adoption", "ev-product-leadership", "pf-full"]),
        "."
      ]},

      {"type": "li", "segments": [
        "Incumbent must have the ability to ",
        ph("a-exec-consulting", "blend front-facing, executive level consulting skills",
           ["ev-exec-alignment", "ev-e2e-client", "ev-storytelling"]),
        " with ",
        ph("a-technical-knowledge", "deep technical knowledge",
           ["ev-ai-agents", "ev-tech-stack", "ev-info-arch", "ev-rd-lab", "ev-ai-retrieval"]),
        " to ",
        ph("a-ai-value", "identify opportunities where AI opportunities can create significant value to the organization",
           ["ev-ai-product", "ev-insights", "pf-ai-roadmap"]),
        "."
      ]},

      {"type": "li", "segments": [
        ph("a-managing-teams", "Demonstrated leadership experience managing multidisciplinary teams (consulting, engineering, training, or enablement)",
           ["ev-xfn", "ev-hiring", "ev-team-retention", "ev-org-restructuring"]),
        "."
      ]},

      {"type": "li", "segments": [
        ph("a-enterprise-platforms", "Strong experience with enterprise platforms and productivity tools (e.g., Microsoft 365, Power Platform, ServiceNow, Qualtrics, collaboration tools)",
           ["ev-tooling", "ev-pm-tools", "ev-tech-stack", "ev-tool-migration"]),
        "."
      ]},

      {"type": "li", "segments": [
        ph("a-enabling-ai-adoption", "Demonstrated experience enabling adoption of AI tools and platforms, including training, consulting, or solution design",
           ["ev-adoption", "ev-ai-training", "ev-ai-product"]),
        "."
      ]},

      {"type": "li", "segments": [
        ph("a-translate-user-centered", "Proven ability to translate business needs into practical, user-centered digital solutions",
           ["ev-translator", "ev-experience-design", "ev-design-fluency", "pf-legacy-ux"]),
        "."
      ]},

      {"type": "li", "segments": [
        ph("a-training-programs", "Experience designing and delivering training or enablement programs in higher education or a complex enterprise environment",
           ["ev-curriculum", "ev-training-program", "ev-global"]),
        "."
      ]},

      {"type": "li", "segments": [
        ph("a-communication-change", "Exceptional communication, stakeholder engagement, and change management skills",
           ["ev-speaking", "ev-storytelling", "ev-change", "ev-psych"]),
        "."
      ]},

      {"type": "li", "segments": [
        ph("a-analytical-metrics", "Strong analytical skills with experience using metrics to guide decision-making and demonstrate impact",
           ["ev-metrics", "ev-insights", "ev-decision-frameworks"]),
        "."
      ]},

      {"type": "h2", "text": "Preferred Qualifications"},

      {"type": "li", "segments": [
        ph("a-leading-ai-programs", "Experience leading or supporting AI programs, platforms, or AI-embedded enterprise tools",
           ["ev-ai-product", "ev-ai-agents", "ev-ai-training", "pf-personas"]),
        "."
      ]},

      {"type": "li", "segments": [
        ph("a-ai-governance", "Familiarity with AI governance, ethical use frameworks, and risk considerations",
           ["ev-responsible-ai", "ev-ai-reliability", "ev-regulatory"]),
        "."
      ]},

      {"type": "li", "segments": [
        ph("a-agile-itil-change", "Agile, Scrum, ITIL, or change management experience",
           ["ev-agile", "ev-operating-cadences", "ev-change", "ev-org-restructuring"]),
        "."
      ]},

      {"type": "li", "segments": [
        ph("a-federated-orgs", "Experience working in higher education or similarly complex, federated organizations",
           ["ev-xfn", "ev-wide-industry", "ev-global", "ev-rapid-domain"]),
        "."
      ]},

      {"type": "h2", "text": "Key Accountabilities & responsibilities"},

      {"type": "h3", "text": "1) Integrated Digital Solutions Leadership-"},

      {"type": "p", "segments": [
        ph("a-unified-function", "Provide strategic and operational leadership for digital solutions consulting, solutions engineering, and training as a unified function",
           ["ev-architect-operator", "ev-startup-os", "ev-workstreams", "ev-xfn"]),
        ". ",
        ph("a-service-offerings", "Define and evolve service offerings that intentionally blend consultation, solutioning, and enablement",
           ["ev-gtm", "ev-biz-model", "ev-new-revenue"]),
        ". ",
        ph("a-intake-delivery", "Ensure consistent intake, prioritization, delivery, and documentation of digital solutions engagements across the university",
           ["ev-engagement-ownership", "ev-operating-cadences", "ev-concurrent-pm", "ev-high-stakes-decisions"]),
        "."
      ]},

      {"type": "h3", "text": "2) AI Enablement and Strategy -"},

      {"type": "p", "segments": [
        ph("a-lead-ai-efforts", "Lead the university’s AI enablement efforts within Digital Solutions, including consultation, solution design, training, and diffusion",
           ["ev-ai-training", "ev-adoption", "ev-facilitation", "pf-genai-playbook"]),
        ". ",
        ph("a-program-manager", "Serve as program manager for the AI enablement program, establishing the roadmap, governance-aligned operating model, intake and prioritization mechanisms, and success metrics for AI adoption across the university",
           ["ev-roadmapping", "ev-ai-product", "ev-operating-cadences", "ev-metrics"]),
        ". ",
        ph("a-high-impact-use-cases", "Partner with stakeholders to identify high-impact AI use cases where current processes or jobs can be reengineered to utilize AI",
           ["ev-process-optimization", "ev-workforce-transformation", "ev-agentic-ops", "ev-systems-thinking"]),
        ", ",
        ph("a-responsible-adoption", "guide responsible adoption",
           ["ev-responsible-ai", "ev-psych"]),
        ", and ",
        ph("a-embedded-workflows", "ensure AI tools are embedded into real workflows through consulting, solution design, and training",
           ["ev-agentic-ops", "ev-knowledge-mgmt", "ev-adoption", "pf-prompt-eng", "ev-knowledge-arch-rows"]),
        ". ",
        ph("a-oversee-ai-collab", "Oversee or collaborate closely with AI-focused roles",
           ["ev-mentorship", "ev-xfn", "ev-talent-dev"]),
        " and ",
        ph("a-governance-frameworks", "ensure alignment with institutional AI governance, risk, and ethics frameworks",
           ["ev-responsible-ai", "ev-ai-reliability", "ev-regulatory", "ev-decision-frameworks"]),
        "."
      ]},

      {"type": "h3", "text": "3) Solutions Engineering and Consulting Oversight -"},

      {"type": "p", "segments": [
        ph("a-translate-supportable", "Oversee solution engineering and consulting activities that translate business needs into effective, supportable digital solutions using enterprise platforms (e.g., Microsoft 365, ServiceNow, Qualtrics, Miro, AI platforms)",
           ["ev-translator", "ev-tech-stack", "ev-tooling", "ev-tool-migration"]),
        ". ",
        ph("a-ootb-maintainability", "Ensure solutions emphasize out-of-the-box capabilities, scalability, and maintainability",
           ["ev-pm-system", "ev-playbook", "pf-platform-playbook"]),
        ". ",
        ph("a-guide-teams", "Guide teams in requirements gathering, process mapping",
           ["ev-research", "ev-blueprinting", "pf-global-blueprint", "pf-eraf", "ev-journey-ai"]),
        ", ",
        ph("a-design-testing-handoff", "solution design, testing, and handoff",
           ["ev-testing", "ev-prototyping", "ev-agile", "pf-user-testing"]),
        "."
      ]},

      {"type": "h3", "text": "4) Training, Enablement, and Adoption -"},

      {"type": "p", "segments": [
        ph("a-oversee-training", "Oversee the design and delivery of training and enablement experiences that support adoption of digital and AI-enabled solutions",
           ["ev-curriculum", "ev-ai-training", "ev-facilitation", "ev-training-program"]),
        ". ",
        ph("a-workflow-centered", "Ensure training offerings are practical, workflow-centered, and aligned with real consultative engagements",
           ["ev-adoption", "ev-architect-operator", "ev-e2e-client"]),
        ". ",
        ph("a-instructional-standards", "Establish standards for instructional quality, learning experience design, and measurement of training effectiveness and impact",
           ["ev-training-program", "ev-design-standards", "ev-curriculum", "ev-metrics"]),
        "."
      ]},

      {"type": "h3", "text": "5) Continuous Improvement, Metrics, and Research -"},

      {"type": "p", "segments": [
        ph("a-establish-metrics", "Establish metrics to measure  and report on adoption, impact, and satisfaction across solutions and training",
           ["ev-metrics", "ev-insights", "pf-genai-playbook"]),
        ". ",
        ph("a-monitor-trends", "Monitor trends in digital transformation and AI, evaluate emerging tools",
           ["ev-rd-lab", "ev-ai-tool-eval", "ev-rapid-domain"]),
        ", and ",
        ph("a-improve-service-models", "continuously improve service models",
           ["ev-process-optimization", "ev-root-cause"]),
        ". ",
        ph("a-refine-retire-scale", "Use data and feedback to refine offerings, retire low-value services, and scale high-impact solutions",
           ["ev-insights", "ev-resource-reduction", "ev-new-revenue", "ev-decision-frameworks"]),
        "."
      ]},

      {"type": "h2", "text": "Supervision"},

      {"type": "p", "segments": [
        "This role typically ",
        ph("a-supervises", "supervises managers, leads, and/or senior individual contributors across digital solutions engineering, consulting, training, and AI enablement functions",
           ["ev-hiring", "ev-mentorship", "ev-org-restructuring", "ev-xfn"]),
        ". The Assistant Director is accountable for ",
        ph("a-team-performance", "team performance",
           ["ev-team-retention", "ev-operating-cadences"]),
        ", ",
        ph("a-capacity-planning", "capacity planning",
           ["ev-concurrent-pm", "ev-resource-reduction", "ev-parallel"]),
        ", and ",
        ph("a-professional-development", "professional development",
           ["ev-talent-dev", "ev-coaching", "ev-mentorship"]),
        "."
      ]},
    ]


data = {
  "meta": {
    "candidate": "Ryan Hance",
    "portfolio": "https://www.hance.work/",
    "note": "Pure renderer input. Edit copy here (or in build_data.py). Each highlighted phrase carries the evidence ids that back it."
  },
  "roles": [
    {
      "id": "assistant-director-digital-enablement",
      "tab_label": "Assistant Director, Digital Enablement",
      "job": {
        "company": "Northeastern University",
        "role": "Assistant Director, Digital Enablement",
        "employment": "",
        "location": "Boston, MA (Main Campus) · Hybrid, minimum 3 days per week on site · Req R139231",
        "url": "https://northeastern.wd1.myworkdayjobs.com/careers/job/Boston-MA-Main-Campus/Assistant-Director--Digital-Enablement_R139231",
        "tab_title": "Ryan Hance · Fit Map",
        "candidate_kicker": "Ryan Hance · Fit Map",
        "candidate_lede": ("These are selected notes and resume points from Ryan Hance's career "
                           "experience mapped to the actual Northeastern job description below."),
        "candidate_stat": "Hover over any underlined phrase and select it to see Ryan's experience related to the ask.",
      },
      "jd_prose": jd_prose(),
    },
  ],
  "evidence": evidence,
}

out = os.path.join(HERE, "data.json")
with open(out, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

ids = set()
phrase_ids = []
for role in data["roles"]:
    for b in role["jd_prose"]:
        for seg in b.get("segments", []):
            if isinstance(seg, dict) and "evidence" in seg:
                ids.update(seg["evidence"])
                phrase_ids.append(seg["id"])
missing = [i for i in ids if i not in evidence]
dupes = sorted({p for p in phrase_ids if phrase_ids.count(p) > 1})
print("Wrote", out)
for role in data["roles"]:
    n = sum(1 for b in role["jd_prose"] for s in b.get("segments", []) if isinstance(s, dict) and "id" in s)
    print(f"  {role['id']}: {n} phrases")
print("evidence items:", len(evidence))
print("duplicate phrase ids:", dupes or "none")
unused = [k for k in evidence if k not in ids]
print("unused evidence:", unused or "none")
print("missing evidence refs:", missing or "none")
