/*
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
 */

package org.apache.airavata.xbaya.graph.gui;

import java.awt.Graphics2D;
import java.awt.Point;
import java.awt.Rectangle;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

import javax.swing.SwingUtilities;

import org.apache.airavata.xbaya.XBayaEngine;
import org.apache.airavata.xbaya.graph.Edge;
import org.apache.airavata.xbaya.graph.Graph;
import org.apache.airavata.xbaya.graph.GraphPiece;
import org.apache.airavata.xbaya.graph.Node;
import org.apache.airavata.xbaya.graph.Port;
import org.apache.airavata.xbaya.graph.system.MemoNode;
import org.apache.airavata.xbaya.graph.system.gui.StreamSourceNode;
import org.apache.airavata.xbaya.graph.util.GraphUtil;

public class GraphGUI implements GraphPieceGUI {

    private Graph graph;

    /**
     * @param graph
     */
    public GraphGUI(Graph graph) {
        this.graph = graph;
    }

    /**
     * @see org.apache.airavata.xbaya.graph.gui.GraphPieceGUI#mouseClicked(java.awt.event.MouseEvent,
     *      org.apache.airavata.xbaya.XBayaEngine)
     */
    public void mouseClicked(MouseEvent event, XBayaEngine engine) {
        GraphPiece piece = getGraphPieceAt(event.getPoint());
        if (piece != null && graph.isEditable()) {
            piece.getGUI().mouseClicked(event, engine);
        }
    }

    /**
     * Gets the bounding Rectangle of this Graph.
     * 
     * @return A rectangle indicating this component's bounds
     */
    protected Rectangle getBounds() {
        Rectangle bounds = new Rectangle();
        for (Node node : this.graph.getNodes()) {
            bounds.add(node.getGUI().getBounds());
        }
        final int margin = 10;
        bounds.height += margin;
        bounds.width += margin;
        return bounds;
    }

    /**
     * @param g
     */
    protected void paint(Graphics2D g) {

        // Calcurate the widge of the nodes.
        for (Node node : this.graph.getNodes()) {
            node.getGUI().calculatePositions(g);
        }

        LinkedList<Node> nodes = new LinkedList<Node>(this.graph.getNodes());
        List<MemoNode> memoNodes = GraphUtil.getNodes(this.graph, MemoNode.class);
        nodes.removeAll(memoNodes);

        // Paints the edges before nodes.
        for (Edge edge : this.graph.getEdges()) {
            edge.getGUI().paint(g);
        }

        // Paint regular nodes.
        // The ports are painted from inside of each node.
        for (Node node : nodes) {
            node.getGUI().paint(g);
        }

        // Print memoNodes at last so that they stay on top of everything.
        for (MemoNode node : memoNodes) {
            node.getGUI().paint(g);
        }
    }

    protected StreamSourceNode getStreamSourceAt(Point point) {
        for (Node node : this.graph.getNodes()) {
            // Check the node first
            if (node.getGUI().isIn(point) && node instanceof StreamSourceNode) {
                return (StreamSourceNode) node;
            }
        }
        return null;
    }

    /**
     * Returns the visible object at the specified location. The object is either a Node, a Port, or an Edge.
     * 
     * @param point
     *            The location
     * @return The visible object a the specified location
     */
    protected GraphPiece getGraphPieceAt(Point point) {

        GraphPiece piece = null;

        // Starts from edge because it is drawn first, which means it's at the
        // bottom.
        double minEdgeDist = Double.MAX_VALUE;
        Edge closestEdge = null;
        for (Edge edge : this.graph.getEdges()) {
            double dist = edge.getGUI().getMiddlePosition().distance(point);
            if (dist < minEdgeDist) {
                closestEdge = edge;
                minEdgeDist = dist;
            }
        }
        if (minEdgeDist < 20) {
            piece = closestEdge;
        }

        // Then, each node and ports of it.
        for (Node node : this.graph.getNodes()) {
            // Check the node first
            if (node.getGUI().isIn(point)) {
                piece = node;
            }

            // Find the closest port of this node.
            double minPortDist = Double.MAX_VALUE;
            Port closestPort = null;
            for (Port port : node.getAllPorts()) {
                double dist = port.getGUI().getPosition().distance(point);
                if (dist < minPortDist) {
                    closestPort = port;
                    minPortDist = dist;
                }
            }
            if (minPortDist <= PortGUI.DATA_PORT_SIZE) {
                piece = closestPort;
            }

            // Don't break from this loop because the later ones are drawn at
            // the top of other nodes.
        }
        return piece;
    }

    /**
     * Returns the visible object in the specified area. The objects are either a Node, a Port, or an Edge.
     * 
     * @param rec
     *            area to cover
     * @return The visible object a the specified location
     */
    protected List<Node> getNodesIn(Rectangle rec) {
        ArrayList<Node> pieces = new ArrayList<Node>();

        // Then, each node and ports of it.
        for (Node node : this.graph.getNodes()) {
            Rectangle inter = SwingUtilities.computeIntersection(rec.x, rec.y, rec.width, rec.height, node.getGUI()
                    .getBounds());
            if (inter.width != 0 && inter.height != 0)
                pieces.add(node);
        }

        return pieces;
    }

}