# OS
> 2022.04.12 [🚀](../index/index.md) [despace](index.md) → [Soft](soft.md)

[TOC]

---

> <small>**Operating system (OS)** — EN term. **Операционная система (ОС)** — RU analogue.</small>

An **operating system (OS)** is system software that manages computer hardware, software resources, & provides common services for computer programs.

A **real‑time operating system (RTOS)** is an operating system (OS) for real‑time applications that processes data & events that have critically defined time constraints. An RTOS is distinct from a time sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment. Processing time requirements need to be fully understood & bound rather than just kept as a minimum. All processing must occur within the defined constraints. Real‑time operating systems are event‑driven & preemptive, meaning the OS is capable of monitoring the relevant priority of competing tasks, & make changes to the task priority. Event‑driven systems switch between tasks based on their priorities, while time‑sharing systems switch the task based on clock interrupts.

【**Table.** RTOS comparison】

|*OS*|*CPU architectures*|*Language*|*License*|
|:-|:-|:-|:-|
|**Enea OSE**|ARM, ColdFire, MIPS, PowerPC|Assembler, C, C++|Closed‑source, Proprietary|
|**Linux**| | | |
|**Lynx**| | | |
|**RTEMS**|68k, ARM, Blackfin, ColdFire, H8/300, LatticeMico32, MIPS (Mongoose-V), Nios II, OpenRISC, PowerPC, SuperH, SPARC (ERC32, LEON), TI C3x/C4x, x86| |Open source, Modified GPL|
|**ThreadX**| | | |
|**VxWorks**|ARM, MIPS, PowerPC, RISC-V, SH-4, 86, x86-64| |Proprietary|



<p style="page-break-after:always"> </p>

## RTOS list

### Enea OSE

> <https://www.enea.com/products-services/operating-systems/enea-ose>  
> <https://en.wikipedia.org/wiki/ENEA_AB>  
> [Datasheet ❐](f/soft/enea_nfv_access_datasheet.pdf)

The Enea family of real‑time operating systems was first released in 2009.

The Enea Operating System Embedded (OSE) is a family of real‑time, microkernel, embedded operating system created by Bengt Eliasson for ENEA AB, which at the time was collaborating with Ericsson to develop a multi‑core system using Assembly, C, & C++. Enea OSE Multicore Edition is based on the same microkernel architecture. The kernel design that combines the advantages of both traditional asymmetric multiprocessing (AMP) & symmetric multiprocessing (SMP). Enea OSE Multicore Edition offers both AMP & SMP processing in a hybrid architecture. OSE supports many processors, mainly 32‑bit. These include the ColdFire, ARM, PowerPC, & MIPS based system on a chip (SoC) devices.

The Enea OSE family features three OSs: OSE (also named OSE Delta) for processors by ARM, PowerPC, & MIPS, OSEck for various DSP's, & OSE Epsilon for minimal devices, written in pure assembly (ARM, ColdFire, C166, M16C, 8051). OSE is a closed‑source proprietarily licensed software released on 2018.03.20. OSE uses events (or signals) in the form of messages passed to & from processes in the system. Messages are stored in a queue attached to each process. A link handler mechanism allows signals to be passed between processes on separate machines, over a variety of transports. The OSE signalling mechanism formed the basis of an open‑source inter‑process kernel design project named LINX.



### RTEMS

> <http://www.rtems.org/>  
> <https://en.wikipedia.org/wiki/RTEMS>

**Real‑Time Executive for Multiprocessor Systems (RTEMS)**, formerly Real‑Time Executive for Missile Systems, & then Real‑Time Executive for Military Systems, is a real‑time operating system (RTOS) designed for embedded systems. It is free & open‑source software.

Development began in the late 1980s with early versions available via File Transfer Protocol (ftp) as early as 1993. OAR Corporation is currently managing the RTEMS project in cooperation with a steering committee which includes user representatives.

RTEMS is designed for real‑time, embedded systems & to support various open application programming interface (API) standards including Portable Operating System Interface (POSIX) & µITRON. The API now known as the Classic RTEMS API was originally based on the Real‑Time Executive Interface Definition (RTEID) specification. RTEMS includes a port of the FreeBSD Internet protocol suite (TCP/IP stack) & support for various file systems including Network File System (NFS) & File Allocation Table (FAT).

RTEMS provides extensive [multi-processing ⎆](https://docs.rtems.org/branches/master/c-user/multiprocessing.html) & [memory-management services ⎆](https://docs.rtems.org/branches/master/posix-users/memory_managment.html), & even a [System‑database ⎆](https://docs.rtems.org/branches/master/posix-users/system_database.html) alongside many other facilities. It has [extensive documentation ⎆](https://docs.rtems.org/).




### VxWorks

> <https://www.windriver.com/products/vxworks>  
> <https://en.wikipedia.org/wiki/VxWorks>



<p style="page-break-after:always"> </p>

## Docs & links
|Navigation|
|:--|
|**[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC (OE+SGM)](sc.md)**·КА】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Drawing](drawing.md)**·Чертёж, **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[N&B](nnb.md)**·БНО, **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[TRL](trl.md)**·УГТ, **[Way](way.md)**·Пути|
|*Sections & pages*|
|**【[Guidance, Navigation & Control (GNC)](gnc.md)】**<br> [CAN](can.md)・ [LVDS](lvds.md)・ [MIL‑STD‑1553](mil_std_1553.md) (МКО)・ [OS](os.md)・ [RS‑232, 422, 485](rs_xxx.md)・ [SpaceWire](spacewire.md)・ [АСН, САН](ans.md)・ [БНО](nnb.md)[MIL‑STD‑1553](mil_std_1553.md) (МКО)[БАППТ](eas.md)・ [БКС](cable.md)・ [БУ](eas.md)・ [БШВ](time.md)・ [Гироскоп](iu.md)・ [Дальномер](doppler.md) (ИСР)・ [ДМ](iu.md)・ [ЗД](sensor.md)・ [Компьютер](obc.md) (ЦВМ, БЦВМ)・ [Магнитометр](sensor.md)・ [МИХ](mic.md)・ [МКО](mil_std_1553.md)・ [ПО](soft.md)・ [ПНА, ПОНА, ПСНА](devd.md)・ [СД](sensor.md)・ [Система координат](coord_sys.md)・ [СОСБ](devd.md)|
|**【[On-board computer (OBC)](obc.md)】**<br> … <br>• • •<br> **RU:** [OS](os.md)・ [МПК-003](obc_lst.md) (9)・ [БИВК-МР](obc_lst.md) (8)・ [МАРС 4](obc_lst.md) (8)・ [БИВК-Р](obc_lst.md) (7.1)・ [МАРС 7](obc_lst.md) (6)・ [МПК-002](obc_lst.md) (3.9)・ [ЦВМ-12](obc_lst.md) (2.2)・ [БКУ_SXPA](obc_lst.md) (0.35)・ [БИВК-МН](бивк‑мн.md) () *([ЦВМ22](obc_lst.md) (2.1))*|
|**【[Software](soft.md)】**<br> [ASP](asp.md)・ [Blender](blender.md)・ [C](plang.md)・ [Cosmographia](cosmographia.md)・ [DOORS](doors.md)・ [DWG](cad_f.md)・ [GIMP](gimp.md)・ [Git](git.md)・ [IGES](cad_f.md)・ [ISIS](isis.md)・ [JT](cad_f.md)・ [NGT](neogeography_toolkit.md)・ [NX](nx.md)・ [Octave](gnu_octave.md)・ [OS](os.md)・ [PDF](pdf.md)・ [Python](plang.md)・ [R](plang.md)・ [SPICE](spice.md)・ [STEP](cad_f.md)・ [STL](stk.md)・ [SVG](cad_f.md)・ [Syncthing](syncthing.md)・ [SysML](sysml.md)・ [Teamcenter](teamcenter.md)・ [Система управления версиями](vcs.md)・ [ХРИП](adra.md)|

   1. Docs: …
   1. <https://en.wikipedia.org/wiki/Real-time_operating_system>