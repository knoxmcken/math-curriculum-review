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
    search_tool = TavilySearchTool()
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
        description=f"""Using the detailed information gathered from the research task, create a comprehensive unified curriculum report for {program} programs in {country}.
        
        Your report must be based SOLELY on the information provided from the previous step.
        
        Your report should include:
        1. Executive Summary
        2. Overview of {program} landscape in {country}
        3. Detailed curriculum analysis:
           - Common core courses across universities
           - Popular elective tracks
           - Program duration and structure
           - Entry requirements
        4. A detailed breakdown for each of the 5-8 universities identified, with their specific key features.
        5. Comparative analysis highlighting similarities and differences between the SPECIFIC universities found.
        6. A proposed ideal program structure based on best practices identified in the research.
        7. A complete references section with all sources and URLs cited.
        
        Ensure every piece of information is properly attributed to its source.""",
        agent=summarizer_agent,
        expected_output=f"""A comprehensive curriculum report of 2000-3000 words, covering the specific {program} 
        programs found in {country}. The report MUST contain real university names, specific curriculum details, and proper references with URLs. It should not contain any placeholder data.""",
        context=[research_task]
    )
    
    # Task 3: Validate and finalize the report
    validation_task = Task(
        description=f"""Review and validate the curriculum report generated by the summarizer. Ensure it meets all requirements based on the original research data. Then, output the FINAL, corrected curriculum report.

        VALIDATION CHECKLIST:
        1. Factual Accuracy & Citations:
           - All universities mentioned are real and match the research data.
           - All claims are backed by proper citations with REAL URLs from the research task.
           - There are no unsourced claims or placeholder URLs like "Source A".

        2. Completeness Check:
           - The report includes the 5-8 universities from the initial research.
           - Each university's curriculum details are covered as per the research findings.
           - No universities or key details are missing.

        3. Placeholder Check:
           - The report MUST NOT contain any placeholder information like "University A", "City, State", or generic course lists. All data must be specific and drawn from the research.

        4. Structure & Formatting:
           - The report follows the required structure (Executive Summary, Analysis, etc.).
           - The proposed program is clearly articulated and based on evidence from the research.

        If ANY requirement is not met, you must correct the report before finalizing.
        
        OUTPUT: Provide the complete, validated, and corrected curriculum report. This is the final output, not a validation summary.""",
        agent=validator_agent,
        expected_output=f"""The final, polished curriculum report for {program} programs in {country}. This comprehensive 2000-3000 word document must contain specific data for 5-8 universities, including real names, detailed curricula, and properly formatted citations with valid URLs. It must be free of any placeholder content.""",
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
    
    try:
        # Create and run the crew
        crew = create_university_research_crew(country, program)
        crew.kickoff()
        
        # The final report is available in the output of the last task
        result = crew.tasks[-1].output
        
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
