import plotly.graph_objects as go


def crear_piramide(edades, hombres, mujeres, anio):

    total_hombres = int(hombres.sum())
    total_mujeres = int(mujeres.sum())

    hombres_neg = -hombres

    maximo = max(hombres.max(), mujeres.max())
    limite = maximo * 1.25

    fig = go.Figure()

    # -----------------------------
    # HOMBRES
    # -----------------------------
    fig.add_trace(

        go.Bar(

            y=edades,

            x=hombres_neg,

            orientation="h",

            name="Masculino",

            marker=dict(

                color="steelblue",

                line=dict(
                    color="black",
                    width=1
                )

            ),

            hovertemplate="<b>Masculino</b><br>%{y}<br>%{customdata:,}<extra></extra>",

            customdata=hombres

        )

    )

    # -----------------------------
    # MUJERES
    # -----------------------------
    fig.add_trace(

        go.Bar(

            y=edades,

            x=mujeres,

            orientation="h",

            name="Femenino",

            marker=dict(

                color="orchid",

                line=dict(
                    color="black",
                    width=1
                )

            ),

            hovertemplate="<b>Femenino</b><br>%{y}<br>%{x:,}<extra></extra>"

        )

    )

    fig.update_layout(

        title=dict(

            text=f"<b>Pirámide Poblacional de Salaverry</b><br>Año {anio}",

            x=0.5,

            font=dict(size=22)

        ),

        template="plotly_white",

        height=720,

        barmode="relative",

        bargap=0.08,

        dragmode="pan",

        legend=dict(

            orientation="h",

            y=1.05,

            x=0.38,

            font=dict(size=13)

        ),

        margin=dict(

            l=70,

            r=70,

            t=90,

            b=60

        ),

        annotations=[

            dict(

                x=0.03,

                y=0.98,

                xref="paper",

                yref="paper",

                text=f"<b>Masculino</b><br>{total_hombres:,}",

                showarrow=False,

                bgcolor="steelblue",

                bordercolor="black",

                borderwidth=1,

                borderpad=8,

                font=dict(

                    color="white",

                    size=15

                )

            ),

            dict(

                x=0.97,

                y=0.98,

                xref="paper",

                yref="paper",

                text=f"<b>Femenino</b><br>{total_mujeres:,}",

                showarrow=False,

                bgcolor="orchid",

                bordercolor="black",

                borderwidth=1,

                borderpad=8,

                font=dict(

                    color="white",

                    size=15

                )

            )

        ]

    )

    # Línea central

    fig.add_vline(

        x=0,

        line_width=2,

        line_color="black"

    )

    # Eje X

    fig.update_xaxes(

        range=[-limite, limite],

        tickformat=",",

        zeroline=False,

        showgrid=True,

        gridcolor="lightgray"

    )

    # Mostrar valores absolutos en el eje X

    fig.update_xaxes(
        tickvals=[-limite, -limite/2, 0, limite/2, limite],
        ticktext=[
            f"{int(limite):,}",
            f"{int(limite/2):,}",
            "0",
            f"{int(limite/2):,}",
            f"{int(limite):,}"
        ]
    )

    fig.update_yaxes(

        title="Grupo de edad",

        showgrid=False

    )

    return fig