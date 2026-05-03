# 🏏 IPL Match Explainer Agent

## 📌 Project Overview  
This project is an Agentic AI system built using Python and Google ADK that analyzes IPL match data and explains why a team won or lost based on statistical performance. It uses numerical match data such as runs, wickets, overs, and phase-wise performance (Powerplay, Middle Overs, Death Overs) to generate clear cricket-style insights.

## 🚀 Features  
- 📊 Analyzes match data using numerical inputs  
- 🧠 Explains why a team won or lost  
- ⚡ Phase-wise breakdown (Powerplay, Middle, Death overs)  
- 📈 Run rate comparison between teams  
- 🏆 Final match result explanation  
- 🤖 Built using Agentic AI (LLM-based reasoning)

## 🛠️ Tech Stack  
Python, Pandas, Google ADK, Gemini Flash Model, Agent-based architecture

## ⚙️ How It Works  
User provides match data → Agent processes it using tools (run rate calculation, phase analysis, team comparison) → AI generates explanation of match outcome focusing on key turning points like run rate drops, wicket losses, and death overs performance.

## 🧪 Example Input  
Team A: 185/5 (20 overs), Powerplay: 55, Middle: 85, Death: 45  
Team B: 160/9 (20 overs), Powerplay: 42, Middle: 70, Death: 48  

## 📊 Example Output  
Team A won the match due to stronger middle overs performance and better run rate consistency. Team B lost wickets in clusters during middle overs which reduced their chase momentum. Death overs recovery was not enough to reach the target.

## ▶️ How to Run  
python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  
python main.py  

## 🔮 Future Improvements  
- Add win prediction model  
- Integrate real IPL dataset  
- Build live match analysis system  
- Add web dashboard for visualization  

## 👨‍💻 Author  
Built as an Agentic AI cricket analytics project for learning and demonstration purposes.
