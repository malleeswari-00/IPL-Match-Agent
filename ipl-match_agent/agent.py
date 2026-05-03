import pandas as pd
from google.adk.agents import Agent

def calculate_run_rate(runs: int, overs: int) -> dict:
    """
    Calculates the run rate for a team given the total runs scored and total overs batted.

    Args:
        runs (int): The total runs scored by the team.
        overs (int): The total number of overs batted.

    Returns:
        dict: A dictionary containing the 'status' ('success' or 'error') and the calculated 'run_rate'.
    """
    try:
        if overs <= 0:
            return {'status': 'error', 'message': 'Overs must be greater than 0.'}
        run_rate = runs / overs
        return {'status': 'success', 'run_rate': run_rate}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def analyze_phases(phase_data: dict) -> dict:
    """
    Analyzes the phase-wise runs of a team (powerplay, middle, death).

    Args:
        phase_data (dict): A dictionary containing runs scored in different phases.
                           Expected keys: 'powerplay', 'middle', 'death'.

    Returns:
        dict: A dictionary with 'status' and the analysis identifying strengths/weaknesses across phases.
    """
    try:
        powerplay = phase_data.get('powerplay', 0)
        middle = phase_data.get('middle', 0)
        death = phase_data.get('death', 0)
        
        analysis = {
            'powerplay_performance': 'good' if powerplay > 45 else 'poor',
            'middle_overs_momentum': 'maintained' if middle > 70 else 'dropped',
            'death_overs_finish': 'strong' if death > 40 else 'weak',
            'total_phase_runs': powerplay + middle + death
        }
        return {'status': 'success', 'analysis': analysis}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def compare_teams(teamA: dict, teamB: dict) -> dict:
    """
    Compares the performance metrics of two teams based on run rate, wickets, and total runs.

    Args:
        teamA (dict): Data for Team A. Expected keys: 'runs', 'wickets', 'overs'.
        teamB (dict): Data for Team B. Expected keys: 'runs', 'wickets', 'overs'.

    Returns:
        dict: A dictionary containing 'status' and a comparison of the teams.
    """
    try:
        comparison = {}
        comparison['winner'] = 'Team A' if teamA.get('runs', 0) > teamB.get('runs', 0) else ('Team B' if teamB.get('runs', 0) > teamA.get('runs', 0) else 'Tie')
        
        teamA_overs = teamA.get('overs', 20)
        teamB_overs = teamB.get('overs', 20)
        
        comparison['teamA_run_rate'] = teamA.get('runs', 0) / teamA_overs if teamA_overs > 0 else 0
        comparison['teamB_run_rate'] = teamB.get('runs', 0) / teamB_overs if teamB_overs > 0 else 0
        comparison['wickets_diff'] = abs(teamA.get('wickets', 0) - teamB.get('wickets', 0))
        
        return {'status': 'success', 'comparison': comparison}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def identify_key_reasons(match_data: dict) -> dict:
    """
    Identifies key reasons for a team's win or loss based on match data.

    Args:
        match_data (dict): The complete match data containing team stats and phase data.

    Returns:
        dict: A dictionary containing 'status' and the key reasons for the outcome.
    """
    try:
        reasons = []
        teamA = match_data.get('teamA', {})
        teamB = match_data.get('teamB', {})
        
        teamA_phases = teamA.get('phases', {})
        teamB_phases = teamB.get('phases', {})
        
        if teamA_phases.get('middle', 0) < teamB_phases.get('middle', 0):
            reasons.append("Team A's run rate dropped in the middle overs compared to Team B.")
            
        if teamA_phases.get('death', 0) > teamB_phases.get('death', 0):
            reasons.append("Team B conceded too many runs in the death overs.")
            
        return {'status': 'success', 'reasons': reasons}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

root_agent = Agent(
    model='gemini-flash-latest',
    name='ipl_match_explainer_agent',
    description="An agent that analyzes IPL match data and explains why a team won or lost using statistical insights.",
    instruction="""You are an expert IPL match analyst. 
Analyze the provided match data using your tools.
Compare performance metrics (run rate, wickets, phases) between the teams.
Identify the key tactical successes or failures for both teams.
Generate a concise natural language explanation summarizing why a team won or lost. Focus on specifics like run rate drops in middle overs or conceding too many runs in death overs.""",
    tools=[calculate_run_rate, analyze_phases, compare_teams, identify_key_reasons]
)
