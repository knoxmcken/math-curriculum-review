"""
University Program Research Crew using CrewAI
Searches for university programs, summarizes curricula, and validates the final report
"""

import sys
import click
from crewai import Agent, Task, Crew, Process
# Add Tavily Search tool
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, TavilySearchTool

def create_university_research_crew(country: str, program: str):
    """
    Create a crew of agents to research university programs
    
    Args:
        country: The country where universities are located
        program: The degree program to research (e.g., "BSc Mathematics")
    """
    
    # Initialize tools
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()
    
    # Agent 1: Web Search Agent
    web_search_agent = Agent(
        role='University Program Researcher',
        goal=f'Find comprehensive information about {program} programs in {country}, including curriculum details, course structures, and university information',
        backstory=f"""You are an expert educational researcher specializing in higher education programs.
        Your expertise lies in finding detailed information about university programs, their curricula,
        course requirements, and institutional details. You have a keen eye for identifying reputable
        universities and extracting relevant program information.""",
        verbose=True,
        allow_delegation=False,
        tools=[search_tool, scrape_tool],
        max_iter=15
    )
    
    # Agent 2: Summarizer Agent
    summarizer_agent = Agent(
        role='Curriculum Summarizer',
        goal=f'Synthesize all gathered information about {program} programs into a comprehensive, unified curriculum report',
        backstory="""You are a skilled academic analyst who excels at synthesizing complex educational
        information from multiple sources. You can identify common patterns, unique features, and create
        comprehensive summaries that capture the essence of multiple university programs. Your reports
        are clear, well-structured, and informative.""",
        verbose=True,
        allow_delegation=False
    )
    
    # Agent 3: Validator Agent
    validator_agent = Agent(
        role='Report Validator',
        goal='Ensure the final report meets all quality standards: proper citations, complete university coverage, and includes a proposed program structure',
        backstory="""You are a meticulous quality assurance specialist with extensive experience in
        academic reporting. You ensure that all reports meet strict standards including proper referencing,
        comprehensive coverage of all sources, and actionable recommendations. You have a sharp eye for
        missing information and inconsistencies.""",
        verbose=True,
        allow_delegation=False
    )
    
    # Task 1: Research universities and programs
    research_task = Task(
        description=f"""Research and gather detailed information about {program} programs in {country}.
        
        Your research should include:
        1. Identify at least 5-8 universities offering {program} in {country}
        2. For each university, gather:
           - University name and website
           - Program structure and duration
           - Core curriculum and required courses
           - Elective options
           - Entry requirements
           - Any unique features or specializations
        3. Collect URLs and sources for all information found
        
        Be thorough and ensure you capture comprehensive curriculum details from each institution.""",
        agent=web_search_agent,
        expected_output=f"""A detailed collection of information about {program} programs from multiple 
        universities in {country}, including curriculum details, course structures, and source URLs."""
    )
    
    # Task 2: Summarize findings
    summarize_task = Task(
        description=f"""Create a comprehensive unified curriculum report for {program} programs in {country}.
        
        Your report should include:
        1. Executive Summary
        2. Overview of {program} landscape in {country}
        3. Detailed curriculum analysis:
           - Common core courses across universities
           - Popular elective tracks
           - Program duration and structure
           - Entry requirements
        4. University-by-university breakdown with key features
        5. Comparative analysis highlighting similarities and differences
        6. A proposed ideal program structure based on best practices identified
        7. Complete references section with all sources cited
        
        Ensure every piece of information is properly attributed to its source.""",
        agent=summarizer_agent,
        expected_output=f"""A comprehensive curriculum report (2000-3000 words) covering all {program} 
        programs found in {country}, with proper structure, analysis, and complete references.""",
        context=[research_task]
    )
    
    # Task 3: Validate and finalize the report
    validation_task = Task(
        description="""Review and validate the curriculum report against these requirements, then output the FINAL CURRICULUM REPORT:
        
        VALIDATION CHECKLIST:
        1. References Check:
           - All universities mentioned have citations
           - URLs and sources are properly formatted
           - No unsourced claims exist
        
        2. Coverage Check:
           - All universities researched are included in the report
           - Each university has curriculum details covered
           - No programs are missing from the summary
        
        3. Proposed Program Check:
           - A clear proposed program structure is included
           - The proposal is based on evidence from the research
           - The proposal includes course structure and rationale
        
        If ANY requirement is not met, make the necessary corrections to the report.
        
        OUTPUT: Provide the complete, validated curriculum report - NOT a validation assessment, but the actual final curriculum report itself.""",
        agent=validator_agent,
        expected_output=f"""The complete, final curriculum report for {program} programs in {country} - a comprehensive 2000-3000 word document with all sections, proper citations, and validated content.""",
        context=[research_task, summarize_task]
    )
    
    # Create the crew
    crew = Crew(
        agents=[web_search_agent, summarizer_agent, validator_agent],
        tasks=[research_task, summarize_task, validation_task],
        process=Process.sequential,
        verbose=True
    )
    
    return crew


@click.command()
@click.option('-c', '--country', default='USA', help='The country to research universities in.')
@click.option('-p', '--program', default='BSc in Mathematics', help='The program to research.')
def main(country, program):
    """Main function to run the university research crew"""
    
    print(f"\n{'='*80}")
    print(f"University Program Research Crew")
    print(f"Country: {country}")
    print(f"Program: {program}")
    print(f"{'='*80}\n")
    
    # Create and run the crew
    crew = create_university_research_crew(country, program)
    
    try:
        result = crew.kickoff()
        
        print(f"\n{'='*80}")
        print("RESEARCH COMPLETE")
        print(f"{'='*80}\n")
        print(result)
        
        # Save the result to a file
        filename = f"{program.replace(' ', '_')}_{country.replace(' ', '_')}_report.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(result))
        print(f"\n\nReport saved to: {filename}")
        
    except Exception as e:
        print(f"\nError during crew execution: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
