# Enhanced Plotly chart with unique markers, larger fonts, and thicker lines
fig = go.Figure()

# Symbol list (ensuring uniqueness)
symbols = ["circle", "square", "diamond", "cross", "x", "triangle-up"]

# Plot entries with unique markers
traces = [
    ("Strain X - py4dstem", "StrainX_py4dstem", "blue", "dash", symbols[0]),
    ("Strain X - CC-ST-AE", "StrainX_CC-ST-AE", "orange", "solid", symbols[1]),
    ("Strain Y - py4dstem", "StrainY_py4dstem", "blue", "dash", symbols[2]),
    ("Strain Y - CC-ST-AE", "StrainY_CC-ST-AE", "orange", "solid", symbols[3]),
    ("Shear - py4dstem", "Shear_py4dstem", "blue", "dash", symbols[4]),
    ("Shear - CC-ST-AE", "Shear_CC-ST-AE", "orange", "solid", symbols[5]),
]

for name, col, color, dash, symbol in traces:
    fig.add_trace(
        go.Scatter(
            x=df_clean["BKG_noise_intensity"],
            y=df_clean[col],
            mode="lines+markers",
            name=name,
            line=dict(color=color, dash=dash, width=3),
            marker=dict(symbol=symbol, size=10),
        )
    )

# Update layout with larger fonts
fig.update_layout(
    title="MAE vs BKG Noise Intensity",
    xaxis_title="Background Noise Intensity (%)",
    yaxis_title="Mean Absolute Error (*1e-3)",
    legend_title="Measurement Type",
    template="plotly_white",
    font=dict(size=16),
    legend=dict(font=dict(size=14)),
    margin=dict(l=80, r=40, t=60, b=60),
)

# Save updated chart
enhanced_html_path = "/mnt/data/mae_vs_bkg_noise_plot_enhanced.html"
fig.write_html(enhanced_html_path)

enhanced_html_path
