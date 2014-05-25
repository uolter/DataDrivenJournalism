# World cup
    
    import pandas as pd
    from IPython.core.display import HTML
    
    teamA = 'Messico'
    teamB = 'Camerun'
    medals = pd.read_csv("medals.csv")
    # data.head()
    
    medals.columns = ['team', 'first', 'second', 'third', 'fourth', 'tot']
    
    def show_best_team(teamA, teamB, data):
        
        totA = data[data.team == teamA ]['tot']
        totB = data[data.team == teamB]['tot']
        
        totA = int(totA) if len(totA)>0 else 0
        totB = int(totB) if len(totB)>0 else 0 
        
        if totA > totB:
            print '%s won %d medals while %s won %d medals' % (teamA, totA, teamB, totB)
        else:
            print '%s won %d medals while %s won %d medals' % (teamB, totB, teamA, totA)
       
    
    def show_best_winner(teamA, teamB, data):
        totA = data[data.team == teamA ]['first']
        totB = data[data.team == teamB]['first']
        
        totA = int(totA) if len(totA)>0 else 0
        totB = int(totB) if len(totB)>0 else 0 
        
        if totA > totB:
            return '%s won %d championships while %s won %d championships' % (teamA, totA, teamB, totB)
        else:
            return '%s won %d championships while %s won %d championships' % (teamB, totB, teamA, totA)
            
    text = show_best_team(teamA, teamB, medals) 
    HTML(text)
    text = show_best_winner(teamA, teamB, medals)
    HTML(text)

    Camerun won 0 medals while Messico won 0 medals





Camerun won 0 championships while Messico won 0 championships




    # world cup history
    
    data = pd.read_csv("history.csv")
    # data.head()
    
    def show_team_history(team):
        team_hist = pd.concat(
            (data[data.firstp == team],
             data[data.secodp == team],
             data[data.thirdp == team],
             data[data.fourthp == team])
        )
        
        if not team_hist.empty:
        
            print '%s History in the world cup' %team
            return team_hist.sort(['Year'])
    
    show_team_history(teamA)


    show_team_history(teamB)


    cal = pd.read_csv("calendar.csv")
    # cal.head()
    
    def show_matches(team_a, team_b):
            metches_ab = cal[cal.team_a == team_a][cal.team_b == team_b]
            metches_ba = cal[cal.team_a == team_b][cal.team_a == team_a]
            
            metches = pd.concat((metches_ab, metches_ba))
            
            if not metches.empty:
                print '%s and %s direct metches.' %(team_a, team_b)
                return metches
            else:
                print '%s and %s never met before' %(team_a, team_b)
    
    show_matches(teamA, teamB)

    Messico and Camerun never met before



    # Read the teams and for each team get the medals and the number of victories
    
    teams = pd.read_csv("teams.csv")
    
    teams.head()
    
    # merging dataframe: team with medals
    team_and_medals = pd.merge(teams, medals, how='left', on='team')
    
    team_and_medals.head(10)
    #for t in teams.index:
        # print teams.ix[t].team
        # for each team get the num of medals
        #    m = medals[medals.team == teams.ix[t].team]




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>team</th>
      <th>first</th>
      <th>second</th>
      <th>third</th>
      <th>fourth</th>
      <th>tot</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>           Algeria</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>         Argentina</td>
      <td>  2</td>
      <td>  2</td>
      <td>  0</td>
      <td>  0</td>
      <td>  4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>         Australia</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>            Belgio</td>
      <td>  0</td>
      <td>  0</td>
      <td>  0</td>
      <td>  1</td>
      <td>  1</td>
    </tr>
    <tr>
      <th>4</th>
      <td> Bosnia Erzegovina</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>           Brasile</td>
      <td>  5</td>
      <td>  2</td>
      <td>  2</td>
      <td>  1</td>
      <td> 10</td>
    </tr>
    <tr>
      <th>6</th>
      <td>           Camerun</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>              Cile</td>
      <td>  0</td>
      <td>  0</td>
      <td>  1</td>
      <td>  0</td>
      <td>  1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>          Colombia</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>     Corea del Sud</td>
      <td>  0</td>
      <td>  0</td>
      <td>  0</td>
      <td>  1</td>
      <td>  1</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 6 columns</p>
</div>




    players = pd.read_csv("players.csv", sep='\t')
    
    players.head()




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pos</th>
      <th>Giocatore</th>
      <th>eta</th>
      <th>Pres.</th>
      <th>Gol</th>
      <th>Nazionale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> P</td>
      <td>       Manuel Neuer</td>
      <td> 28</td>
      <td>  45</td>
      <td> 0</td>
      <td> Germania</td>
    </tr>
    <tr>
      <th>1</th>
      <td> P</td>
      <td> Roman Weidenfeller</td>
      <td> 33</td>
      <td>   1</td>
      <td> 0</td>
      <td> Germania</td>
    </tr>
    <tr>
      <th>2</th>
      <td> D</td>
      <td>       Philipp Lahm</td>
      <td> 30</td>
      <td> 105</td>
      <td> 5</td>
      <td> Germania</td>
    </tr>
    <tr>
      <th>3</th>
      <td> D</td>
      <td>    Per Mertesacker</td>
      <td> 29</td>
      <td>  96</td>
      <td> 4</td>
      <td> Germania</td>
    </tr>
    <tr>
      <th>4</th>
      <td> D</td>
      <td>     Marcell Jansen</td>
      <td> 28</td>
      <td>  45</td>
      <td> 3</td>
      <td> Germania</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 6 columns</p>
</div>




    # older and younger player
    #players.ix[players['eta'].argmax()]
    print 'Older Players.'
    players.sort(['eta'], ascending=[0])[:5]

    Older Players.





<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pos</th>
      <th>Giocatore</th>
      <th>eta</th>
      <th>Pres.</th>
      <th>Gol</th>
      <th>Nazionale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>184</th>
      <td> P</td>
      <td>    Noel Valladares</td>
      <td> 37</td>
      <td> 120</td>
      <td>   0</td>
      <td>       Honduras</td>
    </tr>
    <tr>
      <th>174</th>
      <td> C</td>
      <td> Giorgos Karagounis</td>
      <td> 37</td>
      <td> 132</td>
      <td>  10</td>
      <td>         Grecia</td>
    </tr>
    <tr>
      <th>158</th>
      <td> A</td>
      <td>      Didier Drogba</td>
      <td> 36</td>
      <td>  99</td>
      <td>  63</td>
      <td> Costa d’Avorio</td>
    </tr>
    <tr>
      <th>259</th>
      <td> D</td>
      <td>  Daniel Van Buyten</td>
      <td> 36</td>
      <td>  77</td>
      <td>  10</td>
      <td>         Belgio</td>
    </tr>
    <tr>
      <th>107</th>
      <td> P</td>
      <td>   Gianluigi Buffon</td>
      <td> 36</td>
      <td> 139</td>
      <td>-114</td>
      <td>         Italia</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 6 columns</p>
</div>




    print 'Younger Players.'
    players.sort(['eta'], ascending=[1])[:5]

    Younger Players.





<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pos</th>
      <th>Giocatore</th>
      <th>eta</th>
      <th>Pres.</th>
      <th>Gol</th>
      <th>Nazionale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>648</th>
      <td> D</td>
      <td>    Frank Bagnack</td>
      <td> 18</td>
      <td> 0</td>
      <td> 0</td>
      <td>     Camerun</td>
    </tr>
    <tr>
      <th>398</th>
      <td> D</td>
      <td>        Luke Shaw</td>
      <td> 18</td>
      <td> 1</td>
      <td> 0</td>
      <td> Inghilterra</td>
    </tr>
    <tr>
      <th>273</th>
      <td> C</td>
      <td>    Adnan Januzaj</td>
      <td> 19</td>
      <td> 0</td>
      <td> 0</td>
      <td>      Belgio</td>
    </tr>
    <tr>
      <th>555</th>
      <td> D</td>
      <td>     José Giménez</td>
      <td> 19</td>
      <td> 4</td>
      <td> 0</td>
      <td>     Uruguai</td>
    </tr>
    <tr>
      <th>287</th>
      <td> D</td>
      <td> Cristian Ramírez</td>
      <td> 19</td>
      <td> 2</td>
      <td> 0</td>
      <td>     Ecuador</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 6 columns</p>
</div>




    # best scorer
    #players.ix[players['Gol'].argmax()]
    players.sort(['Gol'], ascending=[0])[:5]




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pos</th>
      <th>Giocatore</th>
      <th>eta</th>
      <th>Pres.</th>
      <th>Gol</th>
      <th>Nazionale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18 </th>
      <td> A</td>
      <td>    Miroslav Klose</td>
      <td> 35</td>
      <td> 131</td>
      <td> 68</td>
      <td>       Germania</td>
    </tr>
    <tr>
      <th>158</th>
      <td> A</td>
      <td>     Didier Drogba</td>
      <td> 36</td>
      <td>  99</td>
      <td> 63</td>
      <td> Costa d’Avorio</td>
    </tr>
    <tr>
      <th>654</th>
      <td> A</td>
      <td>      Samuel Eto'o</td>
      <td> 33</td>
      <td> 115</td>
      <td> 55</td>
      <td>        Camerun</td>
    </tr>
    <tr>
      <th>588</th>
      <td> A</td>
      <td> Cristiano Ronaldo</td>
      <td> 29</td>
      <td> 110</td>
      <td> 49</td>
      <td>     Portogallo</td>
    </tr>
    <tr>
      <th>10 </th>
      <td> C</td>
      <td>    Lukas Podolski</td>
      <td> 28</td>
      <td> 112</td>
      <td> 46</td>
      <td>       Germania</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 6 columns</p>
</div>




    # worst goolkeeper
    #players.ix[players['Gol'].argmin()]
    players.sort(['Gol'], ascending=[1])[:5]




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pos</th>
      <th>Giocatore</th>
      <th>eta</th>
      <th>Pres.</th>
      <th>Gol</th>
      <th>Nazionale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>107</th>
      <td> P</td>
      <td> Gianluigi Buffon</td>
      <td> 36</td>
      <td> 139</td>
      <td>-114</td>
      <td>            Italia</td>
    </tr>
    <tr>
      <th>367</th>
      <td> P</td>
      <td>      Júlio César</td>
      <td> 34</td>
      <td>  76</td>
      <td> -54</td>
      <td>           Brasile</td>
    </tr>
    <tr>
      <th>38 </th>
      <td> P</td>
      <td>    Asmir Begović</td>
      <td> 26</td>
      <td>  28</td>
      <td> -26</td>
      <td> Bosnia Erzegovina</td>
    </tr>
    <tr>
      <th>108</th>
      <td> P</td>
      <td> Salvatore Sirigu</td>
      <td> 27</td>
      <td>   7</td>
      <td>  -8</td>
      <td>            Italia</td>
    </tr>
    <tr>
      <th>368</th>
      <td> P</td>
      <td>           Victor</td>
      <td> 31</td>
      <td>   6</td>
      <td>  -4</td>
      <td>           Brasile</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 6 columns</p>
</div>




    teamA_players = players[players.Nazionale == teamA]
    teamB_players = players[players.Nazionale == teamB]
    
    # avarage age
    print 'Mean age %s: %f' %(teamA, teamA_players['eta'].mean())
    print 'Mean age %s: %f' %(teamB, teamB_players['eta'].mean())

    Mean age Messico: 27.421053
    Mean age Camerun: 26.434783



    print 'Mean goal scored by %s players: %f' %(teamA, teamA_players[teamA_players.Pos <> 'P']['Gol'].mean())
    print 'Mean goal scored by %s players: %f' %(teamB, teamB_players[teamB_players.Pos <> 'P']['Gol'].mean())

    Mean goal scored by Messico players: 2.235294
    Mean goal scored by Camerun players: 4.250000



    
