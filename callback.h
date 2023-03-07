#ifndef __CALLBACK_H__
#define __CALLBACK_H__

#ifdef __cplusplus
extern "C"{
#endif

#define EXPORT __declspec(dllexport)

// 回调函数原型
typedef int (*callback_t)(char*);

extern callback_t callback;
extern int doCallback(char* s);

// 注册回调函数
EXPORT int setCallback(callback_t s);

EXPORT void c_free(void *ptr);

#ifdef __cplusplus
}
#endif
#endif