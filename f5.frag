#version 430

uniform float time;

void main()
{
    float w = 1;
    float a = 1.4;
    gl_FragColor = vec4(0.5, 0.4, 0.3, sin(w * time + a));
}