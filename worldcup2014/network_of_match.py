import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


def main():

    calendar = pd.read_csv("calendar.csv")
    G=nx.Graph()


    for r in calendar.index:

        G.add_edge(calendar.ix[r].team_a, calendar.ix[r].team_b)
        #print calendar.ix[r].team_a, calendar.ix[r].team_b

    nx.draw_networkx(G, node_size=100, node_color='b', label='World cup past matches')
    plt.show()


    print 'Diameter:', nx.diameter(G)

    print 'Degree Centrality '
    degree_centrality = nx.degree_centrality(G)
    for w in sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:10]:
        print w, degree_centrality[w]

    print
    print 'Betweenness Centrality'
    betweenness_centrality = nx.betweenness_centrality(G)
    for w in sorted(betweenness_centrality, key=betweenness_centrality.get, reverse=True)[:10]:
        print w, betweenness_centrality[w]



if __name__ == '__main__':

    main()