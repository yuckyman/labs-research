---
title: "Model-Order Reduction of a Dynamic 1D Spatial Discretized SOFC Model"
authors:
  - "Matthis de Lange"
  - "Pablo Segovia"
  - "Rudy R Negenborn"
  - "Lindert van Biert"
year: 2025
journal: "ECS Meeting Abstracts"
doi: "10.1149/ma2025-03178mtgabs"
url: "https://doi.org/10.1149/ma2025-03178mtgabs"
lab: "radboud-university"
faculty:
  - "Floris de Lange"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  <jats:p>This work presents a reduced-order 1D spatial discretized SOFC model for the implementation of a thermal stress-aware model predictive control strategy. Preserving dynamic spatial temperature behaviour is crucial as a thermal stress indicator. The results highlight a trade-off between model complexity and spatial temperature accuracy. The reduced-order model maintains the same dynamic behaviour as the original SOFC model, enabling the development of safety margins for thermal stress-aware operation.</jats:p>
                    <jats:p/>
                    <jats:p>
                      <jats:bold>1. Introduction</jats:bold>
                    </jats:p>
                    <jats:p>SOFCs are a promising solution to mitigate polluting emissions. Especially in the maritime sector, the SOFC is seen as part of the solution due to its high efficiency and the ability to internally convert various alternative fuels. The SOFC can operate on hydrogen, methanol, ammonia, and the transition fuel methane, leading to overall low emissions [1,2].</jats:p>
                    <jats:p>SOFCs are primarily used for steady-state applications, like the electricity grid, where only small or slow load changes occur [3]. In contrast, maritime applications demand fast and significant load changes due to highly dynamic power profiles. Unlike conventional diesel propulsion systems, SOFCs struggle with rapid responses to such loads. To address this, SOFCs can be complemented with faster-responding power sources like batteries, engines, and PEMFCs. However, current SOFC systems used in vessels are relatively low power [3], highlighting the need to enhance their transient operation capabilities for large-scale applications.</jats:p>
                    <jats:p>
                      The challenge lies in their susceptibility to damage during transient operation. Violating operational limits (e.g., fuel or air utilization, cell potential, or temperature) or inducing thermal stress in the
                      <jats:italic>Positive-electrode Electrolyte Negative-electrode</jats:italic>
                      (PEN) structure due to temperature gradients can cause damage [4]. Since these effects are unmeasurable, SOFCs are operated conservatively and slowly to ensure safety and longevity, resulting in limited response to dynamic loads [3].
                    </jats:p>
                    <jats:p>This research explores thermal-stress-aware power modulation by predicting and constraining local temperature gradients during dynamic operation using Model Predictive Control (MPC). A reduced 1D spatially discretized model of the SOFC’s PEN structure is developed for MPC applications. The original model in [5] includes 968 dynamic states, which poses a real-time feasibility challenge for optimization-based MPC. By reducing the number of states while preserving spatial temperature dynamics, the model will be more efficient for MPC implementation.</jats:p>
                    <jats:p>The state reduction involves two steps. A common assumption is that the dynamics, which are much faster than the desired sample time, are approximated in steady-state [5]. This allows for efficient sampling at the desired sample time. Furthermore, the discretization order (number of control volumes) of the spatial distribution can be reduced. This will significantly impact the accuracy of the temperature distribution. Therefore, the effect of the discretization order on the active PEN temperature distribution and temperature gradient is evaluated in a case study.</jats:p>
                    <jats:p>
                      <jats:bold>2. Methodology</jats:bold>
                    </jats:p>
                    <jats:p>
                      The 1D spatially discretized SOFC model, as described in [5], comprises several components. Chemistry equations and mass balances govern reaction rates and molar gas concentrations, while electrochemistry determines the current density and cell potential. Energy balances are used to resolve the temperature dynamics. The resulting system can be modelled as a system of
                      <jats:italic>Ordinary Differential Equations</jats:italic>
                      (ODE) as given in Appendix A (Eq. 1), with the variables described in Appendix B Table 1.
                    </jats:p>
                    <jats:p>
                      This work focuses on temperature and power dynamics, which are adequately approximated using a 1-second time step. In contrast, the time scales of the chemistry, mass balance, and electrochemistry are much smaller and are approximated as being in steady-state. This results in a static mass balance, as presented in Appendix A (Eq. 2), which is solved for each control volume to determine the molar flow. The solution has to ensure a uniform cell potential across all control volumes, with the total current density summing to the requested current as described in Appendix A (Eq. 3) and (Eq. 4), respectively. The resulting model is formulated as a system of
                      <jats:italic>Differential-Algebraic Equations</jats:italic>
                      (DAE) system given in Appendix A (Eq. 5). The reaction rates are chosen as algebraic states since they uniquely define the molar flow, current density, and cell potential. This simplification reduces the original ODE model with 968 states to a DAE model with 368 differential states and 150 algebraic states.
                    </jats:p>
                    <jats:p>The solvability of a DAE system is determined by its index number. MPC-compatible time-integration schemes require a DAE index of one, meaning the algebraic equations need to be differentiated only once for a solution [6]. This requirement is defined by the condition in (Eq. 6) of Appendix A.</jats:p>
                    <jats:p>The 1D spatial discretized SOFC model can be further simplified by reducing the number of control volumes at the cost of degrees of freedom in the solution. Various reductions, as given in Appendix B Table 2, are simulated to validate the DAE model and to show the sensitivity of the discretization reduction with respect to the modelling accuracy.</jats:p>
                    <jats:p>The reduced order SOFC models are simulated interconnected with the balance of plant of the benchmark system as presented in [7] and an input trajectory for the molar flows and the current. The SOFC model stacks 100 cells. The results of these simulations are compared to the simulation result of the full ODE model, to quantify the ability of the reduced-order models to capture the local temperature behaviour, spatial temperature gradient and temporal temperature gradient. The 0D model, as presented in [8], is included in the results as well, as this has already been implemented in an MPC as a prediction model, successfully regulating the system with the full ODE SOFC model as the simulation model.</jats:p>
                    <jats:p>
                      <jats:bold>3. Results</jats:bold>
                    </jats:p>
                    <jats:p>The inputs for the system are determined to ensure that the 0D SOFC system operates the system at setpoint for the power (800,1600) [W], fuel utilization between (0.60,0.80) [-] and an air outlet temperature of (923,1103) [K]. The setpoint is varied to obtain dynamic trajectories of the system. In Appendix C Figure 1, one can verify that the resulting dynamic trajectories adhere to the operational constraints and feasible region of the SOFC system. Furthermore, the figure emphasizes the influence of internal processes on electrical power, as the power generated by the 0D model differs significantly from that of the 1D model.</jats:p>
                    <jats:p>
                      The local temperature behaviour of the active PEN area of the SOFC system is of interest in this research. With the spatial temperature distribution, one can obtain the spatial temperature gradient by differentiating the temperature over the spatial dimension and the temporal temperature gradient by differentiating with respect to time. The temperature distribution, with respect to space, can be projected as a distribution between the maximum and minimum temperature, resulting in an area over time, as is shown in Appendix C Figure 2a. The corresponding
                      <jats:italic>key performance indicator</jats:italic>
                      (KPI) is defined as the intersection of the temperature area of the full ODE model and the temperature area of the reduced-order models, given in Appendix C Figure 2d. Following the same approach, the projected area for the spatial and temporal gradients is obtained, with the corresponding KPIs.
                    </jats:p>
                    <jats:p>The results show that more control volumes result in a wider spread of the active PEN temperature distribution and the spatial temperature gradient, giving more degrees of freedom for local behaviour. This is confirmed by the significantly higher peaks in the temporal temperature gradient of the higher-order modules. The general behaviour of the reduced order models is still the same as that of the full ODE model, as the temperature distributions of the reduced order models stay inside the distribution of the full ODE model. This is, however, not the case for the 0D ODE model, as the temporal temperature gradient is overestimated at certain time instances compared to the full ODE model.</jats:p>
                    <jats:p>It should be noted that the DAE model with 50 control volumes still covers 99.96% of the original temperature distribution, 99.96% of the spatial temperature gradient and 98.75% of the temporal temperature gradient resulting from the full ODE model. Reducing the number of control volumes, degrade the results to 81.57% for the active PEN temperature distribution, 61.03% for the spatial temperature gradient, and 76.43% for the temporal temperature gradient. To compare, the currently used 0D model only covers 44.02% of the temperature distribution, 0% of the spatial temperature gradient (as the gradient is constant due to the lumped nature of the model) and 27.95% of the temporal temperature gradient.</jats:p>
                    <jats:p>When implementing reduced-order models in an MPC application, it is important to recognize that lower-order models tend to underestimate both temperature distribution and temperature gradients. However, because the DAE model more accurately preserves overall temperature dynamics, it provides a better foundation to define safe operation margins for the MPC compared to the 0D ODE model. As a result, the MPC can leverage this advantage for faster dynamic power tracking.</jats:p>
                    <jats:p>Lastly, the index-1 condition in (Eq. 6) of Appendix A for the DAE models is numerically checked. Since there are as many algebraic equations as algebraic states, the Jacobian of the algebraic equations with respect to the algebraic states is a square matrix. This matrix is full rank, and therefore, the index-1 condition is satisfied.</jats:p>
                    <jats:p>
                      <jats:bold>4. Conclusion</jats:bold>
                    </jats:p>
                    <jats:p>
                      This research demonstrates the simplification of a 1D spatially discretised SOFC model by reducing the number of state variables while preserving its 1D spatial discretization and dynamic behaviour. The key findings are as follows:
                      <jats:list list-type="bullet">
                        <jats:list-item>
                          <jats:p>The resulting DAE model accurately approximates the dynamics of the 1D ODE model for time scales greater than 1 second, e.g., the temperature dynamics are approximated over 98%.</jats:p>
                        </jats:list-item>
                        <jats:list-item>
                          <jats:p>Further reducing the model order by decreasing the spatial discretization lowers the approximation accuracy. A reduction from 968 to 53 states leads to a 19% decrease in active PEN temperature distribution, a 39% reduction in the spatial temperature gradient, and a 24% reduction in the temporal temperature gradient.</jats:p>
                        </jats:list-item>
                        <jats:list-item>
                          <jats:p>The DAE model preserves temperature dynamics over time, simplifying the development of safe margins to compensate for reduced accuracy.</jats:p>
                        </jats:list-item>
                      </jats:list>
                    </jats:p>
                    <jats:p>The next step involves integrating the 1D DAE model into the MPC optimization framework. Here, the computation time can be balanced versus the prediction accuracy to determine the most suitable spatial discretization order for the MPC application.</jats:p>
                    <jats:p>In future research, standard model-order reduction techniques (e.g. the proper orthogonal decomposition) could be utilized to further minimize the number of model states or enhance the accuracy of spatial distribution predictions.</jats:p>
                    <jats:p>
                      <jats:bold>Acknowledgement</jats:bold>
                    </jats:p>
                    <jats:p>The research is supported by the European Consortium ‘HELENUS’ (Grant agreement ID: 1010567). The HELENUS Project aims to demonstrate the applicability, scalability and fuel-flexibility of highly efficient solid oxide fuel cells (SOFCs) in various large ship applications.</jats:p>
                    <jats:p>
                      <jats:bold>References</jats:bold>
                      <jats:table-wrap id="table--001" orientation="portrait" position="anchor">
                        <jats:table content-type="mtgabstract">
                          <jats:thead content-type="mtgabstract">
                            <jats:tr>
                              <jats:th colspan="1" content-type="border-bottom align-left" rowspan="1">
                                [1]
                                <jats:break/>
                              </jats:th>
                              <jats:th colspan="1" content-type="border-bottom" rowspan="1">
                                O. B. Inal, C. Deniz, Assessment of fuel cell types for ships: Based on multi-criteria decision analysis,
                                <jats:italic>Journal of Cleaner Production</jats:italic>
                                , vol. 265, pp. 121734, 2020.
                                <jats:break/>
                              </jats:th>
                            </jats:tr>
                          </jats:thead>
                          <jats:tbody>
                            <jats:tr>
                              <jats:td colspan="1" content-type="row-heading" rowspan="1">
                                [2]
                                <jats:break/>
                              </jats:td>
                              <jats:td colspan="1" rowspan="1">
                                L. van Biert, M. Godjevac, K. Visser, P. Aravind, A review of fuel cell systems for maritime applications,
                                <jats:italic>Journal of Power Sources,</jats:italic>
                                vol. 327, pp. 345–364, 2016.
                                <jats:break/>
                              </jats:td>
                            </jats:tr>
                            <jats:tr>
                              <jats:td colspan="1" content-type="row-heading" rowspan="1">
                                [3]
                                <jats:break/>
                              </jats:td>
                              <jats:td colspan="1" rowspan="1">
                                B. Van Veldhuizen, L. Van Biert, P. V. Aravind and K. Visser, Solid oxide fuel cells for marine applications,
                                <jats:italic>International Journal of Energy Research,</jats:italic>
                                vol. 1, 2023.
                                <jats:break/>
                              </jats:td>
                            </jats:tr>
                            <jats:tr>
                              <jats:td colspan="1" content-type="row-heading" rowspan="1">
                                [4]
                                <jats:break/>
                              </jats:td>
                              <jats:td colspan="1" rowspan="1">
                                F. Baldi, L. Wang, M. Pérez-Fortes, and F. Maréchal, A cogeneration system based on solid oxide and proton exchange membrane fuel cells with hybrid storage for off-grid applications.
                                <jats:italic>Frontiers in Energy Research</jats:italic>
                                , vol. 6, pp. 139, 2019.
                                <jats:break/>
                              </jats:td>
                            </jats:tr>
                            <jats:tr>
                              <jats:td colspan="1" content-type="row-heading" rowspan="1">
                                [5]
                                <jats:break/>
                              </jats:td>
                              <jats:td colspan="1" rowspan="1">
                                L. Van Biert, M. Godjevac, K. Visser and P. Aravind, Dynamic modelling of a direct internal reforming solid oxide fuel cell stack based on single cell experiments,
                                <jats:italic>Applied Energy,</jats:italic>
                                vol. 250, pp. 976-990, 2019.
                                <jats:break/>
                              </jats:td>
                            </jats:tr>
                            <jats:tr>
                              <jats:td colspan="1" content-type="row-heading" rowspan="1">
                                [6]
                                <jats:break/>
                              </jats:td>
                              <jats:td colspan="1" rowspan="1">
                                C. Pantelides, R. Sargent, and V. Vassiliadis, Optimal control of multistage systems described by high-index differential-algebraic equations, 1994, In R. Bulirsch and D. Kraft (eds.),
                                <jats:italic>Computational Optimal Control</jats:italic>
                                , Birkhäuser, Basel.
                                <jats:break/>
                              </jats:td>
                            </jats:tr>
                            <jats:tr>
                              <jats:td colspan="1" content-type="row-heading" rowspan="1">
                                [7]
                                <jats:break/>
                              </jats:td>
                              <jats:td colspan="1" rowspan="1">
                                M.H. de Lange, P. Segovia, R.R. Negenborn, L. van Biert, A framework for advanced safety-constraint control of solid oxide fuel cell systems in maritime applications, in: Proceedings of the 16th European SOFC &amp; SOE Forum, EFCF, Lucerne, Switzerland, 2024.
                                <jats:break/>
                              </jats:td>
                            </jats:tr>
                            <jats:tr>
                              <jats:td colspan="1" content-type="row-heading" rowspan="1">
                                [8]
                                <jats:break/>
                              </jats:td>
                              <jats:td colspan="1" rowspan="1">
                                L. van Biert, P. Segovia Castillo, A. Haseltalab and R.R. Negenborn, A reduced-order model of a solid oxide fuel cell stack for model predictive control, in
                                <jats:italic>Proceedings of the International Ship Control Systems Symposium</jats:italic>
                                , 2022.
                                <jats:break/>
                              </jats:td>
                            </jats:tr>
                          </jats:tbody>
                        </jats:table>
                      </jats:table-wrap>
                    </jats:p>
                    <jats:p>
                      <jats:inline-formula/>
                    </jats:p>
                    <jats:p>Figure 1</jats:p>
                    <jats:p/>
fulltext_available: false
fulltext_source: "none"
created: "2025-11-24T09:28:56.967920"
---

# Model-Order Reduction of a Dynamic 1D Spatial Discretized SOFC Model

## Abstract

<jats:p>This work presents a reduced-order 1D spatial discretized SOFC model for the implementation of a thermal stress-aware model predictive control strategy. Preserving dynamic spatial temperature behaviour is crucial as a thermal stress indicator. The results highlight a trade-off between model complexity and spatial temperature accuracy. The reduced-order model maintains the same dynamic behaviour as the original SOFC model, enabling the development of safety margins for thermal stress-aware operation.</jats:p>
                  <jats:p/>
                  <jats:p>
                    <jats:bold>1. Introduction</jats:bold>
                  </jats:p>
                  <jats:p>SOFCs are a promising solution to mitigate polluting emissions. Especially in the maritime sector, the SOFC is seen as part of the solution due to its high efficiency and the ability to internally convert various alternative fuels. The SOFC can operate on hydrogen, methanol, ammonia, and the transition fuel methane, leading to overall low emissions [1,2].</jats:p>
                  <jats:p>SOFCs are primarily used for steady-state applications, like the electricity grid, where only small or slow load changes occur [3]. In contrast, maritime applications demand fast and significant load changes due to highly dynamic power profiles. Unlike conventional diesel propulsion systems, SOFCs struggle with rapid responses to such loads. To address this, SOFCs can be complemented with faster-responding power sources like batteries, engines, and PEMFCs. However, current SOFC systems used in vessels are relatively low power [3], highlighting the need to enhance their transient operation capabilities for large-scale applications.</jats:p>
                  <jats:p>
                    The challenge lies in their susceptibility to damage during transient operation. Violating operational limits (e.g., fuel or air utilization, cell potential, or temperature) or inducing thermal stress in the
                    <jats:italic>Positive-electrode Electrolyte Negative-electrode</jats:italic>
                    (PEN) structure due to temperature gradients can cause damage [4]. Since these effects are unmeasurable, SOFCs are operated conservatively and slowly to ensure safety and longevity, resulting in limited response to dynamic loads [3].
                  </jats:p>
                  <jats:p>This research explores thermal-stress-aware power modulation by predicting and constraining local temperature gradients during dynamic operation using Model Predictive Control (MPC). A reduced 1D spatially discretized model of the SOFC’s PEN structure is developed for MPC applications. The original model in [5] includes 968 dynamic states, which poses a real-time feasibility challenge for optimization-based MPC. By reducing the number of states while preserving spatial temperature dynamics, the model will be more efficient for MPC implementation.</jats:p>
                  <jats:p>The state reduction involves two steps. A common assumption is that the dynamics, which are much faster than the desired sample time, are approximated in steady-state [5]. This allows for efficient sampling at the desired sample time. Furthermore, the discretization order (number of control volumes) of the spatial distribution can be reduced. This will significantly impact the accuracy of the temperature distribution. Therefore, the effect of the discretization order on the active PEN temperature distribution and temperature gradient is evaluated in a case study.</jats:p>
                  <jats:p>
                    <jats:bold>2. Methodology</jats:bold>
                  </jats:p>
                  <jats:p>
                    The 1D spatially discretized SOFC model, as described in [5], comprises several components. Chemistry equations and mass balances govern reaction rates and molar gas concentrations, while electrochemistry determines the current density and cell potential. Energy balances are used to resolve the temperature dynamics. The resulting system can be modelled as a system of
                    <jats:italic>Ordinary Differential Equations</jats:italic>
                    (ODE) as given in Appendix A (Eq. 1), with the variables described in Appendix B Table 1.
                  </jats:p>
                  <jats:p>
                    This work focuses on temperature and power dynamics, which are adequately approximated using a 1-second time step. In contrast, the time scales of the chemistry, mass balance, and electrochemistry are much smaller and are approximated as being in steady-state. This results in a static mass balance, as presented in Appendix A (Eq. 2), which is solved for each control volume to determine the molar flow. The solution has to ensure a uniform cell potential across all control volumes, with the total current density summing to the requested current as described in Appendix A (Eq. 3) and (Eq. 4), respectively. The resulting model is formulated as a system of
                    <jats:italic>Differential-Algebraic Equations</jats:italic>
                    (DAE) system given in Appendix A (Eq. 5). The reaction rates are chosen as algebraic states since they uniquely define the molar flow, current density, and cell potential. This simplification reduces the original ODE model with 968 states to a DAE model with 368 differential states and 150 algebraic states.
                  </jats:p>
                  <jats:p>The solvability of a DAE system is determined by its index number. MPC-compatible time-integration schemes require a DAE index of one, meaning the algebraic equations need to be differentiated only once for a solution [6]. This requirement is defined by the condition in (Eq. 6) of Appendix A.</jats:p>
                  <jats:p>The 1D spatial discretized SOFC model can be further simplified by reducing the number of control volumes at the cost of degrees of freedom in the solution. Various reductions, as given in Appendix B Table 2, are simulated to validate the DAE model and to show the sensitivity of the discretization reduction with respect to the modelling accuracy.</jats:p>
                  <jats:p>The reduced order SOFC models are simulated interconnected with the balance of plant of the benchmark system as presented in [7] and an input trajectory for the molar flows and the current. The SOFC model stacks 100 cells. The results of these simulations are compared to the simulation result of the full ODE model, to quantify the ability of the reduced-order models to capture the local temperature behaviour, spatial temperature gradient and temporal temperature gradient. The 0D model, as presented in [8], is included in the results as well, as this has already been implemented in an MPC as a prediction model, successfully regulating the system with the full ODE SOFC model as the simulation model.</jats:p>
                  <jats:p>
                    <jats:bold>3. Results</jats:bold>
                  </jats:p>
                  <jats:p>The inputs for the system are determined to ensure that the 0D SOFC system operates the system at setpoint for the power (800,1600) [W], fuel utilization between (0.60,0.80) [-] and an air outlet temperature of (923,1103) [K]. The setpoint is varied to obtain dynamic trajectories of the system. In Appendix C Figure 1, one can verify that the resulting dynamic trajectories adhere to the operational constraints and feasible region of the SOFC system. Furthermore, the figure emphasizes the influence of internal processes on electrical power, as the power generated by the 0D model differs significantly from that of the 1D model.</jats:p>
                  <jats:p>
                    The local temperature behaviour of the active PEN area of the SOFC system is of interest in this research. With the spatial temperature distribution, one can obtain the spatial temperature gradient by differentiating the temperature over the spatial dimension and the temporal temperature gradient by differentiating with respect to time. The temperature distribution, with respect to space, can be projected as a distribution between the maximum and minimum temperature, resulting in an area over time, as is shown in Appendix C Figure 2a. The corresponding
                    <jats:italic>key performance indicator</jats:italic>
                    (KPI) is defined as the intersection of the temperature area of the full ODE model and the temperature area of the reduced-order models, given in Appendix C Figure 2d. Following the same approach, the projected area for the spatial and temporal gradients is obtained, with the corresponding KPIs.
                  </jats:p>
                  <jats:p>The results show that more control volumes result in a wider spread of the active PEN temperature distribution and the spatial temperature gradient, giving more degrees of freedom for local behaviour. This is confirmed by the significantly higher peaks in the temporal temperature gradient of the higher-order modules. The general behaviour of the reduced order models is still the same as that of the full ODE model, as the temperature distributions of the reduced order models stay inside the distribution of the full ODE model. This is, however, not the case for the 0D ODE model, as the temporal temperature gradient is overestimated at certain time instances compared to the full ODE model.</jats:p>
                  <jats:p>It should be noted that the DAE model with 50 control volumes still covers 99.96% of the original temperature distribution, 99.96% of the spatial temperature gradient and 98.75% of the temporal temperature gradient resulting from the full ODE model. Reducing the number of control volumes, degrade the results to 81.57% for the active PEN temperature distribution, 61.03% for the spatial temperature gradient, and 76.43% for the temporal temperature gradient. To compare, the currently used 0D model only covers 44.02% of the temperature distribution, 0% of the spatial temperature gradient (as the gradient is constant due to the lumped nature of the model) and 27.95% of the temporal temperature gradient.</jats:p>
                  <jats:p>When implementing reduced-order models in an MPC application, it is important to recognize that lower-order models tend to underestimate both temperature distribution and temperature gradients. However, because the DAE model more accurately preserves overall temperature dynamics, it provides a better foundation to define safe operation margins for the MPC compared to the 0D ODE model. As a result, the MPC can leverage this advantage for faster dynamic power tracking.</jats:p>
                  <jats:p>Lastly, the index-1 condition in (Eq. 6) of Appendix A for the DAE models is numerically checked. Since there are as many algebraic equations as algebraic states, the Jacobian of the algebraic equations with respect to the algebraic states is a square matrix. This matrix is full rank, and therefore, the index-1 condition is satisfied.</jats:p>
                  <jats:p>
                    <jats:bold>4. Conclusion</jats:bold>
                  </jats:p>
                  <jats:p>
                    This research demonstrates the simplification of a 1D spatially discretised SOFC model by reducing the number of state variables while preserving its 1D spatial discretization and dynamic behaviour. The key findings are as follows:
                    <jats:list list-type="bullet">
                      <jats:list-item>
                        <jats:p>The resulting DAE model accurately approximates the dynamics of the 1D ODE model for time scales greater than 1 second, e.g., the temperature dynamics are approximated over 98%.</jats:p>
                      </jats:list-item>
                      <jats:list-item>
                        <jats:p>Further reducing the model order by decreasing the spatial discretization lowers the approximation accuracy. A reduction from 968 to 53 states leads to a 19% decrease in active PEN temperature distribution, a 39% reduction in the spatial temperature gradient, and a 24% reduction in the temporal temperature gradient.</jats:p>
                      </jats:list-item>
                      <jats:list-item>
                        <jats:p>The DAE model preserves temperature dynamics over time, simplifying the development of safe margins to compensate for reduced accuracy.</jats:p>
                      </jats:list-item>
                    </jats:list>
                  </jats:p>
                  <jats:p>The next step involves integrating the 1D DAE model into the MPC optimization framework. Here, the computation time can be balanced versus the prediction accuracy to determine the most suitable spatial discretization order for the MPC application.</jats:p>
                  <jats:p>In future research, standard model-order reduction techniques (e.g. the proper orthogonal decomposition) could be utilized to further minimize the number of model states or enhance the accuracy of spatial distribution predictions.</jats:p>
                  <jats:p>
                    <jats:bold>Acknowledgement</jats:bold>
                  </jats:p>
                  <jats:p>The research is supported by the European Consortium ‘HELENUS’ (Grant agreement ID: 1010567). The HELENUS Project aims to demonstrate the applicability, scalability and fuel-flexibility of highly efficient solid oxide fuel cells (SOFCs) in various large ship applications.</jats:p>
                  <jats:p>
                    <jats:bold>References</jats:bold>
                    <jats:table-wrap id="table--001" orientation="portrait" position="anchor">
                      <jats:table content-type="mtgabstract">
                        <jats:thead content-type="mtgabstract">
                          <jats:tr>
                            <jats:th colspan="1" content-type="border-bottom align-left" rowspan="1">
                              [1]
                              <jats:break/>
                            </jats:th>
                            <jats:th colspan="1" content-type="border-bottom" rowspan="1">
                              O. B. Inal, C. Deniz, Assessment of fuel cell types for ships: Based on multi-criteria decision analysis,
                              <jats:italic>Journal of Cleaner Production</jats:italic>
                              , vol. 265, pp. 121734, 2020.
                              <jats:break/>
                            </jats:th>
                          </jats:tr>
                        </jats:thead>
                        <jats:tbody>
                          <jats:tr>
                            <jats:td colspan="1" content-type="row-heading" rowspan="1">
                              [2]
                              <jats:break/>
                            </jats:td>
                            <jats:td colspan="1" rowspan="1">
                              L. van Biert, M. Godjevac, K. Visser, P. Aravind, A review of fuel cell systems for maritime applications,
                              <jats:italic>Journal of Power Sources,</jats:italic>
                              vol. 327, pp. 345–364, 2016.
                              <jats:break/>
                            </jats:td>
                          </jats:tr>
                          <jats:tr>
                            <jats:td colspan="1" content-type="row-heading" rowspan="1">
                              [3]
                              <jats:break/>
                            </jats:td>
                            <jats:td colspan="1" rowspan="1">
                              B. Van Veldhuizen, L. Van Biert, P. V. Aravind and K. Visser, Solid oxide fuel cells for marine applications,
                              <jats:italic>International Journal of Energy Research,</jats:italic>
                              vol. 1, 2023.
                              <jats:break/>
                            </jats:td>
                          </jats:tr>
                          <jats:tr>
                            <jats:td colspan="1" content-type="row-heading" rowspan="1">
                              [4]
                              <jats:break/>
                            </jats:td>
                            <jats:td colspan="1" rowspan="1">
                              F. Baldi, L. Wang, M. Pérez-Fortes, and F. Maréchal, A cogeneration system based on solid oxide and proton exchange membrane fuel cells with hybrid storage for off-grid applications.
                              <jats:italic>Frontiers in Energy Research</jats:italic>
                              , vol. 6, pp. 139, 2019.
                              <jats:break/>
                            </jats:td>
                          </jats:tr>
                          <jats:tr>
                            <jats:td colspan="1" content-type="row-heading" rowspan="1">
                              [5]
                              <jats:break/>
                            </jats:td>
                            <jats:td colspan="1" rowspan="1">
                              L. Van Biert, M. Godjevac, K. Visser and P. Aravind, Dynamic modelling of a direct internal reforming solid oxide fuel cell stack based on single cell experiments,
                              <jats:italic>Applied Energy,</jats:italic>
                              vol. 250, pp. 976-990, 2019.
                              <jats:break/>
                            </jats:td>
                          </jats:tr>
                          <jats:tr>
                            <jats:td colspan="1" content-type="row-heading" rowspan="1">
                              [6]
                              <jats:break/>
                            </jats:td>
                            <jats:td colspan="1" rowspan="1">
                              C. Pantelides, R. Sargent, and V. Vassiliadis, Optimal control of multistage systems described by high-index differential-algebraic equations, 1994, In R. Bulirsch and D. Kraft (eds.),
                              <jats:italic>Computational Optimal Control</jats:italic>
                              , Birkhäuser, Basel.
                              <jats:break/>
                            </jats:td>
                          </jats:tr>
                          <jats:tr>
                            <jats:td colspan="1" content-type="row-heading" rowspan="1">
                              [7]
                              <jats:break/>
                            </jats:td>
                            <jats:td colspan="1" rowspan="1">
                              M.H. de Lange, P. Segovia, R.R. Negenborn, L. van Biert, A framework for advanced safety-constraint control of solid oxide fuel cell systems in maritime applications, in: Proceedings of the 16th European SOFC &amp; SOE Forum, EFCF, Lucerne, Switzerland, 2024.
                              <jats:break/>
                            </jats:td>
                          </jats:tr>
                          <jats:tr>
                            <jats:td colspan="1" content-type="row-heading" rowspan="1">
                              [8]
                              <jats:break/>
                            </jats:td>
                            <jats:td colspan="1" rowspan="1">
                              L. van Biert, P. Segovia Castillo, A. Haseltalab and R.R. Negenborn, A reduced-order model of a solid oxide fuel cell stack for model predictive control, in
                              <jats:italic>Proceedings of the International Ship Control Systems Symposium</jats:italic>
                              , 2022.
                              <jats:break/>
                            </jats:td>
                          </jats:tr>
                        </jats:tbody>
                      </jats:table>
                    </jats:table-wrap>
                  </jats:p>
                  <jats:p>
                    <jats:inline-formula/>
                  </jats:p>
                  <jats:p>Figure 1</jats:p>
                  <jats:p/>

## Links

- DOI: [10.1149/ma2025-03178mtgabs](https://doi.org/10.1149/ma2025-03178mtgabs)
- URL: [Link](https://doi.org/10.1149/ma2025-03178mtgabs)

## Faculty

- [[radboud-university/faculty#floris-de-lange|Floris de Lange]]
