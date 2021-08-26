import streamlit as st
import plotly.express as px
#from src.image_export import show_export_format


def graph_controls(chart_type, df, dropdown_options, template):
    """
    Function which determines the widgets that would be shown for the different chart types
    :param chart_type: str, name of chart
    :param df: uploaded dataframe
    :param dropdown_options: list of column names
    :param template: str, representation of the selected theme
    :return:
    """
    length_of_options = len(dropdown_options)
    length_of_options -= 1

    plot = px.scatter()

    if chart_type == 'Scatter plots':
        st.sidebar.subheader("Scatterplot Settings")

        try:
            x_values = st.sidebar.selectbox('X axis', index=length_of_options,options=dropdown_options)
            y_values = st.sidebar.selectbox('Y axis',index=length_of_options, options=dropdown_options)
            color_value = st.sidebar.selectbox("Color", index=length_of_options,options=dropdown_options)
            symbol_value = st.sidebar.selectbox("Symbol",index=length_of_options, options=dropdown_options)
            #size_value = st.sidebar.selectbox("Size", index=length_of_options,options=dropdown_options)

            marginalx = st.sidebar.selectbox("Marginal X", index=2,options=['rug', 'box', None,
                                                                         'violin', 'histogram'])
            marginaly = st.sidebar.selectbox("Marginal Y", index=2,options=['rug', 'box', None,
                                                                         'violin', 'histogram'])
            log_x = st.sidebar.selectbox('Log axis on x', options=[False, True])
            log_y = st.sidebar.selectbox('Log axis on y', options=[False, True])
            title = st.sidebar.text_input(label='Title of chart')
            plot = px.scatter(data_frame=df,
                              x=x_values,
                              y=y_values,
                              color=color_value,
                              symbol=symbol_value,                        
                              log_x=log_x, log_y=log_y,marginal_y=marginaly, marginal_x=marginalx,
                              template=template, title=title)

        except Exception as e:
            print(e)


    if chart_type == 'Histogram':
        st.sidebar.subheader("Histogram Settings")

        try:
            x_values = st.sidebar.selectbox('X axis', index=length_of_options,options=dropdown_options)
            y_values = st.sidebar.selectbox('Y axis',index=length_of_options, options=dropdown_options)
            nbins = st.sidebar.number_input(label='Number of bins', min_value=2, value=5)
            color_value = st.sidebar.selectbox("Color", index=length_of_options,options=dropdown_options)

            #barmode = st.sidebar.selectbox('bar mode', options=['group', 'overlay','relative'], index=2)
            #marginal = st.sidebar.selectbox("Marginal", index=2,options=['rug', 'box', None,
            #                                                             'violin', 'histogram'])
            #barnorm = st.sidebar.selectbox('Bar norm', options=[None, 'fraction', 'percent'], index=0)
            hist_func = st.sidebar.selectbox('Histogram aggregation function', index=0,
                                             options=['count','sum', 'avg', 'min', 'max'])
            histnorm = st.sidebar.selectbox('Hist norm', options=[None, 'percent', 'probability', 'density',
                                                                  'probability density'], index=0)
            #hover_name_value = st.sidebar.selectbox("Hover name", index=length_of_options,options=dropdown_options)
            #facet_row_value = st.sidebar.selectbox("Facet row",index=length_of_options, options=dropdown_options,)
            #facet_column_value = st.sidebar.selectbox("Facet column", index=length_of_options,
                                                     #options=dropdown_options)
            cummulative = st.sidebar.selectbox('Cummulative', options=[False, True])
            #log_x = st.sidebar.selectbox('Log axis on x', options=[False, True])
            #log_y = st.sidebar.selectbox('Log axis on y', options=[False, True])
            title = st.sidebar.text_input(label='Title of chart')
            plot = px.histogram(data_frame=df,barmode=barmode,histnorm=histnorm,
                                #marginal=marginal,
                                barnorm=barnorm,
                                #histfunc=hist_func,
                                x=x_values,y=y_values,cumulative=cummulative,
                                color=color_value,
                                #hover_name=hover_name_value,
                                facet_row=facet_row_value,nbins=nbins,
                                facet_col=facet_column_value,
                                #log_x=log_x,
                                #log_y=log_y,
                                template=template, title=title)
        except Exception as e:
            print(e)



    if chart_type == 'Violin plots':
        st.sidebar.subheader('Violin plot Settings')

        try:
            x_values = st.sidebar.selectbox('X axis', index=length_of_options,options=dropdown_options)
            y_values = st.sidebar.selectbox('Y axis',index=length_of_options, options=dropdown_options)
            color_value = st.sidebar.selectbox(label='Color(Selected Column should be categorical)', options=dropdown_options)
            #violinmode = st.sidebar.selectbox('Violin mode', options=['group', 'overlay'])
            #box = st.sidebar.selectbox("Show box", options=[False, True])
            outliers = st.sidebar.selectbox('Show points', options=[False, 'all', 'outliers', 'suspectedoutliers'])
            #hover_name_value = st.sidebar.selectbox("Hover name", index=length_of_options,options=dropdown_options)
            #facet_row_value = st.sidebar.selectbox("Facet row",index=length_of_options, options=dropdown_options,)
            facet_column_value = st.sidebar.selectbox("Facet column", index=length_of_options,
                                                      options=dropdown_options)
            log_x = st.sidebar.selectbox('Log axis on x', options=[False,True])
            log_y = st.sidebar.selectbox('Log axis on y', options=[False,True])
            title = st.sidebar.text_input(label='Title of chart')
            plot = px.violin(data_frame=df,x=x_values,
                             y=y_values,color=color_value,
                             #hover_name=hover_name_value,
                             #facet_row=facet_row_value,
                             facet_col=facet_column_value,
                             #box=box,
                             log_x=log_x, log_y=log_y,
                             #violinmode=violinmode,
                             points=outliers,
                             template=template, title=title)

        except Exception as e:
            print(e)

    if chart_type == 'Box plots':
        st.sidebar.subheader('Box plot Settings')

        try:
            x_values = st.sidebar.selectbox('X axis', index=length_of_options, options=dropdown_options)
            y_values = st.sidebar.selectbox('Y axis', index=length_of_options, options=dropdown_options)
            color_value = st.sidebar.selectbox(label='Color(Selected Column should be categorical)', options=dropdown_options)
            #boxmode = st.sidebar.selectbox('Violin mode', options=['group', 'overlay'])
            outliers = st.sidebar.selectbox('Show outliers', options=[False, 'all', 'outliers', 'suspectedoutliers'])
            #hover_name_value = st.sidebar.selectbox("Hover name", index=length_of_options, options=dropdown_options)
            #facet_row_value = st.sidebar.selectbox("Facet row", index=length_of_options, options=dropdown_options, )
            facet_column_value = st.sidebar.selectbox("Facet column", index=length_of_options,
                                                      options=dropdown_options)
            log_x = st.sidebar.selectbox('Log axis on x', options=[False, True])
            log_y = st.sidebar.selectbox('Log axis on y', options=[False, True])
            notched = st.sidebar.selectbox('Notched', options=[False, True])
            title = st.sidebar.text_input(label='Title of chart')
            plot = px.box(data_frame=df, x=x_values,
                          y=y_values, color=color_value,
                          #hover_name=hover_name_value,facet_row=facet_row_value,
                          facet_col=facet_column_value, notched=notched,
                          log_x=log_x, log_y=log_y, 
                          #boxmode=boxmode, 
                          points=outliers,
                          template=template, title=title)
        except Exception as e:
            print(e)


    if chart_type == 'Pie Charts':
        st.sidebar.subheader('Pie Chart Settings')

        try:
            name_value = st.sidebar.selectbox(label='Name (Selected Column should be categorical)', options=dropdown_options)
            color_value = st.sidebar.selectbox(label='Color(Selected Column should be categorical)', options=dropdown_options)
            value = st.sidebar.selectbox("Value", index=length_of_options, options=dropdown_options)
            hole = st.sidebar.selectbox('Log axis on y', options=[True, False])
            title = st.sidebar.text_input(label='Title of chart')

            plot = px.pie(data_frame=df,names=name_value,hole=hole,
                          values=value,color=color_value, title=title)

        except Exception as e:
            print(e)


    if chart_type == 'custom':
        st.sidebar.subheader("custom Settings")

        try:
            plot = px.box(data_frame=df, x='Site', y='ALT',color='Site',template=template)
            xstart=(df['ALT'].mean()+df['ALT'].std())
            xstart2=(df['ALT'].mean()+2*df['ALT'].std())
            xend=(df['ALT'].mean()-df['ALT'].std())
            xend2=(df['ALT'].mean()-2*df['ALT'].std())
            plot.add_shape(dict(type="rect", x0=-1,x1=6, y0=xstart2, y1=xend2, fillcolor='yellow',
                                opacity=0.1),    row="all",    col="all",)
            plot.add_shape(dict(type="rect", x0=-1,x1=6, y0=xstart, y1=xend, fillcolor='turquoise',
                                opacity=0.1),    row="all",    col="all",)

        except Exception as e:
            print(e)



    st.subheader("Chart")
    st.plotly_chart(plot)
    #show_export_format(plot)