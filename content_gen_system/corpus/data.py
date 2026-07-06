"""
corpus/data.py
---------------
Sample training text for each supported topic. In a production system
this would be replaced with much larger, curated datasets (articles,
documents, or domain-specific text) loaded from files or a database.
"""

TOPICS = {
    "technology": """
        Artificial intelligence is transforming the way businesses operate
        across every industry. Machine learning models can now analyze vast
        amounts of data in seconds, uncovering patterns that would take humans
        weeks to identify. Cloud computing has made powerful infrastructure
        accessible to startups and enterprises alike. Automation is reducing
        repetitive work and allowing teams to focus on creative problem
        solving. As technology continues to evolve, companies that embrace
        innovation will gain a significant competitive advantage. Cybersecurity
        remains a critical concern as more systems move online. Developers are
        building smarter applications that adapt to user behavior in real time.
        The future of technology depends on responsible and ethical development
        practices that keep people at the center of every decision.
    """,
    "health": """
        Maintaining a healthy lifestyle requires a balanced combination of
        proper nutrition, regular exercise, and adequate rest. A well planned
        diet provides the body with essential vitamins and minerals needed for
        energy and recovery. Physical activity strengthens the heart, improves
        mood, and helps maintain a healthy weight. Sleep plays a vital role in
        memory consolidation and overall mental wellbeing. Preventive healthcare,
        including regular checkups, can catch potential issues before they
        become serious. Mental health is just as important as physical health
        and deserves the same level of attention and care. Small consistent
        habits often lead to the most sustainable long term health outcomes.
    """,
    "business": """
        Successful businesses are built on a clear vision, strong leadership,
        and a deep understanding of customer needs. Effective marketing
        strategies help companies reach the right audience with the right
        message at the right time. Financial planning ensures that resources
        are allocated efficiently to support sustainable growth. Building a
        positive company culture improves employee retention and productivity.
        Innovation allows businesses to stay ahead of changing market demands.
        Strong customer relationships are the foundation of long term brand
        loyalty. Entrepreneurs who adapt quickly to feedback are more likely
        to succeed in competitive markets.
    """,
    "education": """
        Education plays a fundamental role in shaping individuals and
        societies. Access to quality learning resources empowers students to
        reach their full potential. Modern classrooms are increasingly
        incorporating technology to create interactive and engaging learning
        experiences. Critical thinking and problem solving skills are essential
        for success in an ever changing world. Teachers who inspire curiosity
        help students develop a lifelong love of learning. Personalized
        learning approaches recognize that every student learns differently.
        Investing in education today builds a stronger and more capable
        generation for tomorrow.
    """,
}
