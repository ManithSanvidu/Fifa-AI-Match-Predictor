import streamlit as st
from tournament_simulator import TournamentSimulator

def render_tournament_tab(models,data):
    st.title("🏆 Tournament Simulator")

    simulator=TournamentSimulator(models,data)

    teams=sorted(data["team"].dropna().unique())

    selected=st.multiselect(
        "Select 16 Teams",
        teams,
        default=teams[:16] if len(teams)>=16 else teams
    )

    if len(selected) != 16:
        st.warning("Please select exactly 16 teams")
        return

    if st.button("Simulate Tournament"):
        results=simulator.simulate_tournament(selected)

        st.subheader("🏁 Round of 16 Winners")
        st.write(results["round_of_16"])

        st.subheader("🥈 Quarter Finals Winners")
        st.write(results["quarter_finals"])

        st.subheader("🥉 Semi Finals Winners")
        st.write(results["semi_finals"])

        st.subheader("🏆 Finalists")
        st.write(results["final"])

        st.success(f"🏆 Champion: {results['champion']}")